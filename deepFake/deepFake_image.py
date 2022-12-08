
import paddle
import argparse
import cv2
import numpy as np
import os
import json
from MobileFaceSwap.models.model import FaceSwap, l2_norm
from MobileFaceSwap.models.arcface import IRBlock, ResNet
from MobileFaceSwap.utils.align_face import back_matrix, dealign, align_img
from MobileFaceSwap.utils.util import paddle2cv, cv2paddle
from MobileFaceSwap.utils.prepare_data import LandmarkModel
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def get_id_emb(id_net, id_img_path):
    id_img = cv2.imread(id_img_path)

    id_img = cv2.resize(id_img, (112, 112))
    id_img = cv2paddle(id_img)
    mean = paddle.to_tensor([[0.485, 0.456, 0.406]]).reshape((1, 3, 1, 1))
    std = paddle.to_tensor([[0.229, 0.224, 0.225]]).reshape((1, 3, 1, 1))
    id_img = (id_img - mean) / std

    id_emb, id_feature = id_net(id_img)
    id_emb = l2_norm(id_emb)

    return id_emb, id_feature


def image_test(args):
    paddle.set_device("gpu" if args.use_gpu else 'cpu')
    faceswap_model = FaceSwap(args.use_gpu)

    id_net = ResNet(block=IRBlock, layers=[3, 4, 23, 3])
    id_net.set_dict(paddle.load('MobileFaceSwap/checkpoints/arcface.pdparams'))

    id_net.eval()

    weight = paddle.load('MobileFaceSwap/checkpoints/MobileFaceSwap_224.pdparams')

    base_path = args.source_img_path.replace('.png', '').replace('.jpg', '').replace('.jpeg', '')
    id_emb, id_feature = get_id_emb(id_net, base_path + '_aligned.png')

    faceswap_model.set_model_param(id_emb, id_feature, model_weight=weight)
    faceswap_model.eval()

    if os.path.isfile(args.target_img_path):
        img_list = [args.target_img_path]
    else:
        img_list = [os.path.join(args.target_img_path, x) for x in os.listdir(args.target_img_path) if x.endswith('png') or x.endswith('jpg') or x.endswith('jpeg')]
    for img_path in img_list:

        origin_att_img = cv2.imread(img_path)
        base_path = img_path.replace('.png', '').replace('.jpg', '').replace('.jpeg', '')
        att_img = cv2.imread(base_path + '_aligned.png')
        att_img = cv2paddle(att_img)
        import time
        
        res, mask = faceswap_model(att_img)
        res = paddle2cv(res)

        if args.merge_result:
            back_matrix = np.load(base_path + '_back.npy')
            mask = np.transpose(mask[0].numpy(), (1, 2, 0))
            res = dealign(res, origin_att_img, back_matrix, mask)
        cv2.imwrite(os.path.join(args.output_dir, os.path.basename(img_path)), res)
    
    return res


def face_align(landmarkModel, image_path, merge_result=False, image_size=224):
    if os.path.isfile(image_path):
        img_list = [image_path]
    else:
        img_list = [os.path.join(image_path, x) for x in os.listdir(image_path) if x.endswith('png') or x.endswith('jpg') or x.endswith('jpeg')]
    for path in img_list:
        img = cv2.imread(path)
        landmark = landmarkModel.get(img)
        if landmark is not None:
            base_path = path.replace('.png', '').replace('.jpg', '').replace('.jpeg', '')
            aligned_img, back_matrix = align_img(img, landmark, image_size)
            # np.save(base_path + '.npy', landmark)
            cv2.imwrite(base_path + '_aligned.png', aligned_img)
            if merge_result:
                np.save(base_path + '_back.npy', back_matrix)


from argparse import Namespace

def deepFake_image_func(source_img_path, target_img_path,
             output_dir = 'results',
             image_size = 224,
             merge_result = True,
             need_align = True,
             use_gpu = False):
    # parser = argparse.ArgumentParser(description="MobileFaceSwap Test")
    # ('--source_img_path', type=str, help='path to the source image')
    # ('--target_img_path', type=str, help='path to the target images')
    # ('--output_dir', type=str, default='results', help='path to the output dirs')
    # ('--image_size', type=int, default=224,help='size of the test images (224 SimSwap | 256 FaceShifter)')
    # ('--merge_result', type=bool, default=True, help='output with whole image')
    # ('--need_align', type=bool, default=True, help='need to align the image')
    # ('--use_gpu', type=bool, default=False)
    if need_align:
        landmarkModel = LandmarkModel(name='landmarks')
        print("after landmarkModel")
        landmarkModel.prepare(ctx_id= 0, det_thresh=0.6, det_size=(640,640))
        face_align(landmarkModel, source_img_path)
        face_align(landmarkModel, target_img_path, merge_result, image_size)
    os.makedirs(output_dir, exist_ok=True)
    
    ### 딥페이크 처리를 위해 dict 형식으로 변환
    args_dict = {
        'source_img_path' : source_img_path,
        'target_img_path' : target_img_path,
        'output_dir' : output_dir,
        'image_size' : image_size,
        'merge_result' : merge_result,
        'need_align' : need_align,
        'use_gpu' : use_gpu
    }
    
    args = convert_dict_to_args(args_dict)
    
    ### 이미지 딥페이크 처리
    return image_test(args=args)

class convert_dict_to_args:
    def __init__(self, args):
        self.source_img_path = args['source_img_path']
        self.target_img_path = args['target_img_path']
        self.output_dir = args['output_dir']
        self.image_size = args['image_size']
        self.merge_result = args['merge_result']
        self.need_align = args['need_align']
        self.use_gpu = args['use_gpu']        

