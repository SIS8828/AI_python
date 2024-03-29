import numpy as np
from collections import OrderedDict
from common.convolution_layer import Convolution
from common.layer import *
class SimpleConvNet:
    '''
    단순한 합성곱 신경망

    conv - relu - pool - affine - relu - affine - sftmax

    parameters

    -----------------
    input_size : 입력크기(MNIST의 경우 784)
    hidden_size_list : 각 은니긍의 뉴런 수를 담은 리스트
    output_size : 출력크기 (MNIST의 경우엔 10)
    activation : 활성화 함수 'relu' 혹은 'sigmoid'
    weight_init_std : 가중치의 표준편차 지정( e.g. 0.01)
                                'relu'나 'he'로 지정하면 'He 초깃값'으로 설정.
                                'sigmoid'로 지정하면 'Xavier' 초기값으로 설정

    '''
    def __init__(self,input_dim=(1,28,28),
                 conv_param = {'filter_num':30, 'filter_size':5 , 'stride':1,'pad':0},
                hidden_size = 100, output_size = 10 , weight_init_std = 0.01):
        filter_num = conv_param['filter_num']
        filter_size = conv_param['filter_ize']
        filter_stride = conv_param['stride']
        filter_pad = conv_param['pad']

        input_size = input_dim[1]

        conv_output_size = (input_size - filter_size + 2 *filter_pad) / filter_stride + 1
        pool_out_size = int(filter_num * (conv_output_size/2) * (conv_output_size/2))


        # 가중치 초기화
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(filter_num,input_dim[0],filter_size,filter_size)
        self.params['b1'] = np.zeros(filter_num)
        self.params['W2'] = weight_init_std * np.random.randn(pool_out_size, hidden_size)
        self.params['b2'] = np.zeros(hidden_size)
        self.params['W3'] = weight_init_std * np.random.randn(hidden_size,output_size)
        self.params['b3'] = np.zeros(output_size)

        # 계층 생성
        self.layers = OrderedDict()
        self.layers['Conv1'] = Convolution(self.params['W1'],self.params['b1'],conv_param['stride'], conv_param['pad'])

        self.layers['Relu1'] = Relu()
        self.layers['Pool1'] = Pooling(pool_h=2,pool_w=2,stride=2)

        self.layers['Affine1'] = Affine(self.params['W2'],self.params['b2'])
        self.layers['Relu2'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W3'], self.params['b3'])

        self.last_layer = SoftmaxWithLoss()


    def predict(self,x):
        for layer in self.layers.values():
            x = layer.forward(x)
            return x

    def loss(self,x,t):
        y = self.predict(x)
        return self.last_layer.forward(y,t)

    def gradient(self,x,t):
        # 순전파
        self.loss(x,t)

        # 역전파
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers :
            dout = layer.backward(dout)

        # 결과저장
        grads = {}
        grads['W1'] = self.layers['Conv1'].dw
        grads['b1'] = self.layers['Conv1'].db

        grads['W2'] = self.layers['Affine1'].dw
        grads['b2'] = self.layers['Affine1'].db

        grads['W3'] = self.layers['Affine2'].dw
        grads['b3'] = self.layers['Affine2'].db

        return  grads
