CONFIG = 'PROD'

BATCH_SIZE = 32
NUM_CLASSES = 10
NUM_DOMAINS = 2
SAVE_DIR = 'weights/'

EPOCHS = 100
SUBSET = None
MODEL_NAME = 'cnn_train_svhn.h5'
LOG_FILE = 'logs/cnn_train_svhn.log'

if CONFIG == 'DEBUG':
    EPOCHS = 10
    SUBSET = 10000
    MODEL_NAME = 'debug.h5'
    LOG_FILE = 'logs/debug.log'
