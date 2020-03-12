import numpy as np
import pandas as pd
import tensorflow as tf
import argparse as arg
import tarfile
import os
import json
import requests
import sys
import shutil
import re
from tqdm import tqdm, trange
from tensorflow.core.protobuf import rewriter_config_pb2
from tensorflow.python.client import device_lib
import time
from datetime import datetime
import csv
