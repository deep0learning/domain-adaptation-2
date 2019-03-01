CONFIG = 'PROD'

BATCH_SIZE = 32
NUM_CLASSES = 10
SAVE_DIR = 'weights/'
IMAGE_SIZE = (32, 32)
CHANNELS = 3
DOMAINS = [
    'mnist',
    'svhn'
]
DOMAINS_IGNORE_LABELS = [
    'mnist'
]

EPOCHS = 1000
SUBSET = 10000

CNN_GRL_MODEL_NAME = 'cnn_grl_merge_train_svhn.h5'
CNN_GRL_LOG_FILE = 'logs/cnn_grl_merge_train_svhn.log'
CNN_MODEL_NAME = 'cnn_train_svhn.h5'
CNN_LOG_FILE = 'logs/cnn_train_svhn.log'

if CONFIG == 'DEBUG':
    EPOCHS = 10
    SUBSET = 1000
    MODEL_NAME = 'debug.h5'
    LOG_FILE = 'logs/debug.log'
    CNN_GRL_MODEL_NAME = MODEL_NAME
    CNN_GRL_LOG_FILE = LOG_FILE
    CNN_MODEL_NAME = MODEL_NAME
    CNN_LOG_FILE = LOG_FILE
