convolutional_block_output1 = [[[[0.,         0.66683817, 0.,         0.,        0.888539,   0.5274254 ],
   [0.,         0.65053666, 0.,         0.,         0.8959285,  0.49965227]],
  [[0.,         0.6312079,  0.,         0.,         0.86362475, 0.47643146],
   [0.,         0.56883204, 0.,        0.,         0.8553412,  0.417093 ]]],
 [[[1.0951002,  0.,         1.5761349,  0.6267836,  0.,         0.,        ],
   [1.3594234,  0.,         1.6074152,  0.6536726,  0.,         0.,        ]],
  [[0.49971345, 0.,         0.9446775,  0.6636579,  0.,         0.,        ],
   [0.98098886, 0.,         1.0731578,  0.6013661,  0.,         0.,        ]]],
 [[[3.2853007,  0.,         4.728405,   1.8803508,  0.,         0.,        ],
   [4.07827,    0.,         4.8222456,  1.9610177,  0.,         0.,        ]],
  [[1.4991404,  0.,         2.8340323,  1.9909737,  0.,         0.,        ],
   [2.9429667,  0.,         3.2194734,  1.8040984,  0.,         0.       ]]]]

convolutional_block_output2 = [[[[0.       , 2.7823157, 0.       , 0.       , 1.6960442, 2.8218517],
   [0.       , 1.5445004, 0.       , 0.       , 2.170656 , 1.3908148]],
  [[0.       , 1.9399526, 0.       , 0.       , 1.4798119, 1.9157798],
   [0.       , 0.       , 0.       , 0.9879823, 1.1234158, 0.       ]]],
 [[[0.,         0.4073585,  0.,         0.60906595, 0.61729676, 0.43824518],
   [0.,         0.4073585,  0.,         0.60906595, 0.61729676, 0.43824518]],
  [[0.,         0.4073585,  0.,         0.60906595, 0.61729676, 0.43824518],
   [0.,         0.4073585,  0.,         0.60906595, 0.61729676, 0.43824518]]],
 [[[2.6159182,  0.,         2.752994,   0.,         0.,         0.,        ],
   [3.4472604,  0.,         2.7312024,  0.03319526, 0.,         0.,        ]],
  [[0.9830525,  0.,         1.6564476,  0.9591365,  0.,         0.,        ],
   [2.5460882,  0.,         1.1291425,  0.,         0.,         0.,        ]]]]


ResNet50_summary =[['InputLayer', (None, 64, 64, 3), 0],
['ZeroPadding2D', (None, 70, 70, 3), 0, ((3, 3), (3, 3))],
['Conv2D', (None, 32, 32, 64), 9472, 'valid', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 32, 32, 64), 256],
['Activation', (None, 32, 32, 64), 0],
['MaxPooling2D', (None, 15, 15, 64), 0, (3, 3), (2, 2), 'valid'],
['Conv2D', (None, 15, 15, 64), 4160, 'valid', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 15, 15, 64), 256],
['Activation', (None, 15, 15, 64), 0],
['Conv2D', (None, 15, 15, 64), 36928, 'same', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 15, 15, 64), 256],
['Activation', (None, 15, 15, 64), 0],
['Conv2D', (None, 15, 15, 256), 16640, 'valid', 'linear', 'GlorotUniform'],
['Conv2D', (None, 15, 15, 256), 16640, 'valid', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 15, 15, 256), 1024],
['BatchNormalization', (None, 15, 15, 256), 1024],
['Add', (None, 15, 15, 256), 0],
['Activation', (None, 15, 15, 256), 0],
['Conv2D', (None, 15, 15, 64), 16448, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 15, 15, 64), 256],
['Activation', (None, 15, 15, 64), 0],
['Conv2D', (None, 15, 15, 64), 36928, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 15, 15, 64), 256],
['Activation', (None, 15, 15, 64), 0],
['Conv2D', (None, 15, 15, 256), 16640, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 15, 15, 256), 1024],
['Add', (None, 15, 15, 256), 0],
['Activation', (None, 15, 15, 256), 0],
['Conv2D', (None, 15, 15, 64), 16448, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 15, 15, 64), 256],
['Activation', (None, 15, 15, 64), 0],
['Conv2D', (None, 15, 15, 64), 36928, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 15, 15, 64), 256],
['Activation', (None, 15, 15, 64), 0],
['Conv2D', (None, 15, 15, 256), 16640, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 15, 15, 256), 1024],
['Add', (None, 15, 15, 256), 0],
['Activation', (None, 15, 15, 256), 0],
['Conv2D', (None, 8, 8, 128), 32896, 'valid', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 8, 8, 128), 512],
['Activation', (None, 8, 8, 128), 0],
['Conv2D', (None, 8, 8, 128), 147584, 'same', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 8, 8, 128), 512],
['Activation', (None, 8, 8, 128), 0],
['Conv2D', (None, 8, 8, 512), 66048, 'valid', 'linear', 'GlorotUniform'],
['Conv2D', (None, 8, 8, 512), 131584, 'valid', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 8, 8, 512), 2048],
['BatchNormalization', (None, 8, 8, 512), 2048],
['Add', (None, 8, 8, 512), 0],
['Activation', (None, 8, 8, 512), 0],
['Conv2D', (None, 8, 8, 128), 65664, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 8, 8, 128), 512],
['Activation', (None, 8, 8, 128), 0],
['Conv2D', (None, 8, 8, 128), 147584, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 8, 8, 128), 512],
['Activation', (None, 8, 8, 128), 0],
['Conv2D', (None, 8, 8, 512), 66048, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 8, 8, 512), 2048],
['Add', (None, 8, 8, 512), 0],
['Activation', (None, 8, 8, 512), 0],
['Conv2D', (None, 8, 8, 128), 65664, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 8, 8, 128), 512],
['Activation', (None, 8, 8, 128), 0],
['Conv2D', (None, 8, 8, 128), 147584, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 8, 8, 128), 512],
['Activation', (None, 8, 8, 128), 0],
['Conv2D', (None, 8, 8, 512), 66048, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 8, 8, 512), 2048],
['Add', (None, 8, 8, 512), 0],
['Activation', (None, 8, 8, 512), 0],
['Conv2D', (None, 8, 8, 128), 65664, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 8, 8, 128), 512],
['Activation', (None, 8, 8, 128), 0],
['Conv2D', (None, 8, 8, 128), 147584, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 8, 8, 128), 512],
['Activation', (None, 8, 8, 128), 0],
['Conv2D', (None, 8, 8, 512), 66048, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 8, 8, 512), 2048],
['Add', (None, 8, 8, 512), 0],
['Activation', (None, 8, 8, 512), 0],
['Conv2D', (None, 4, 4, 256), 131328, 'valid', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 256), 590080, 'same', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 1024), 263168, 'valid', 'linear', 'GlorotUniform'],
['Conv2D', (None, 4, 4, 1024), 525312, 'valid', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 4, 4, 1024), 4096],
['BatchNormalization', (None, 4, 4, 1024), 4096],
['Add', (None, 4, 4, 1024), 0],
['Activation', (None, 4, 4, 1024), 0],
['Conv2D', (None, 4, 4, 256), 262400, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 256), 590080, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 1024), 263168, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 1024), 4096],
['Add', (None, 4, 4, 1024), 0],
['Activation', (None, 4, 4, 1024), 0],
['Conv2D', (None, 4, 4, 256), 262400, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 256), 590080, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 1024), 263168, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 1024), 4096],
['Add', (None, 4, 4, 1024), 0],
['Activation', (None, 4, 4, 1024), 0],
['Conv2D', (None, 4, 4, 256), 262400, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 256), 590080, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 1024), 263168, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 1024), 4096],
['Add', (None, 4, 4, 1024), 0],
['Activation', (None, 4, 4, 1024), 0],
['Conv2D', (None, 4, 4, 256), 262400, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 256), 590080, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 1024), 263168, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 1024), 4096],
['Add', (None, 4, 4, 1024), 0],
['Activation', (None, 4, 4, 1024), 0],
['Conv2D', (None, 4, 4, 256), 262400, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 256), 590080, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 256), 1024],
['Activation', (None, 4, 4, 256), 0],
['Conv2D', (None, 4, 4, 1024), 263168, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 4, 4, 1024), 4096],
['Add', (None, 4, 4, 1024), 0],
['Activation', (None, 4, 4, 1024), 0],
['Conv2D', (None, 2, 2, 512), 524800, 'valid', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 2, 2, 512), 2048],
['Activation', (None, 2, 2, 512), 0],
['Conv2D', (None, 2, 2, 512), 2359808, 'same', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 2, 2, 512), 2048],
['Activation', (None, 2, 2, 512), 0],
['Conv2D', (None, 2, 2, 2048), 1050624, 'valid', 'linear', 'GlorotUniform'],
['Conv2D', (None, 2, 2, 2048), 2099200, 'valid', 'linear', 'GlorotUniform'],
['BatchNormalization', (None, 2, 2, 2048), 8192],
['BatchNormalization', (None, 2, 2, 2048), 8192],
['Add', (None, 2, 2, 2048), 0],
['Activation', (None, 2, 2, 2048), 0],
['Conv2D', (None, 2, 2, 512), 1049088, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 2, 2, 512), 2048],
['Activation', (None, 2, 2, 512), 0],
['Conv2D', (None, 2, 2, 512), 2359808, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 2, 2, 512), 2048],
['Activation', (None, 2, 2, 512), 0],
['Conv2D', (None, 2, 2, 2048), 1050624, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 2, 2, 2048), 8192],
['Add', (None, 2, 2, 2048), 0],
['Activation', (None, 2, 2, 2048), 0],
['Conv2D', (None, 2, 2, 512), 1049088, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 2, 2, 512), 2048],
['Activation', (None, 2, 2, 512), 0],
['Conv2D', (None, 2, 2, 512), 2359808, 'same', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 2, 2, 512), 2048],
['Activation', (None, 2, 2, 512), 0],
['Conv2D', (None, 2, 2, 2048), 1050624, 'valid', 'linear', 'RandomUniform'],
['BatchNormalization', (None, 2, 2, 2048), 8192],
['Add', (None, 2, 2, 2048), 0],
['Activation', (None, 2, 2, 2048), 0],
['AveragePooling2D', (None, 1, 1, 2048), 0],
['Flatten', (None, 2048), 0],
['Dense', (None, 6), 12294, 'softmax']]