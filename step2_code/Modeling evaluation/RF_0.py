import sys
from tensorflow import keras as K
import tensorflow as tf
from tensorflow.keras import regularizers
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
import matplotlib.pyplot as plt
from tensorflow.keras.backend import clear_session
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score


for m in [5,10,15,20,25,30,35,40,45,50]:
    clear_session()
    train_x = pd.read_csv("~/TCGA/Methylation450K/feature_importance_6_15/RF_gredsearch/RF_train_x_0"+"_"+str(m)+".csv")
    train_y = pd.read_csv("~/TCGA/Methylation450K/feature_importance_6_15/RF_gredsearch/RF_train_y_0"+"_"+str(m)+".csv")
    test_x = pd.read_csv("~/TCGA/Methylation450K/feature_importance_6_15/RF_gredsearch/RF_test_x_0"+"_"+str(m)+".csv")
    test_y = pd.read_csv("~/TCGA/Methylation450K/feature_importance_6_15/RF_gredsearch/RF_test_y_0"+"_"+str(m)+".csv")
    ###############################################################  对数据进行标准化
    train_x_zcore=(train_x-train_x.mean(axis=0))/train_x.std(axis=0)
    test_x_zcore=(test_x-train_x.mean(axis=0))/train_x.std(axis=0)
    if m==5:
        b_size = 80
        max_epochs = 50
        clear_session()
        model = K.models.Sequential()
        model.add(K.layers.Dense(units=50, input_dim=train_x_zcore.shape[1],  activation='relu'))
        model.add(K.layers.Dense(units=42, activation='relu'))
        model.add(K.layers.Dense(units=34, activation='relu'))
        model.add(K.layers.Dense(units=25, activation='relu'))
        model.add(K.layers.Dense(units=21,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    if m==10:
        b_size = 80
        max_epochs = 100
        clear_session()
        model = K.models.Sequential()
        model.add(K.layers.Dense(units=100, input_dim=train_x_zcore.shape[1],  activation='relu'))
        model.add(K.layers.Dropout(0.3))
        model.add(K.layers.Dense(units=63, activation='relu'))
        model.add(K.layers.Dropout(0.15))
        model.add(K.layers.Dense(units=25, activation='relu'))
        model.add(K.layers.Dense(units=21,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    if m==15:
        b_size = 50
        max_epochs = 100
        clear_session()
        model = K.models.Sequential()
        model.add(K.layers.Dense(units=170, input_dim=train_x_zcore.shape[1],  activation='relu'))
        model.add(K.layers.Dropout(0.3))
        model.add(K.layers.Dense(units=135, activation='relu'))
        model.add(K.layers.Dropout(0.23))
        model.add(K.layers.Dense(units=100, activation='relu'))
        model.add(K.layers.Dropout(0.16))
        model.add(K.layers.Dense(units=65, activation='relu'))
        model.add(K.layers.Dropout(0.09))
        model.add(K.layers.Dense(units=30, activation='relu'))
        model.add(K.layers.Dropout(0.02))
        model.add(K.layers.Dense(units=21,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    if m==20:
        b_size = 80
        max_epochs = 100
        clear_session()
        model = K.models.Sequential()
        model.add(K.layers.Dense(units=130, input_dim=train_x_zcore.shape[1],  activation='relu'))
        model.add(K.layers.Dropout(0.3))
        model.add(K.layers.Dense(units=78, activation='relu'))
        model.add(K.layers.Dropout(0.15))
        model.add(K.layers.Dense(units=25, activation='relu'))
        model.add(K.layers.Dense(units=21,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    if m==25:
        b_size = 80
        max_epochs = 100
        clear_session()
        model = K.models.Sequential()
        model.add(K.layers.Dense(units=110, input_dim=train_x_zcore.shape[1],  activation='relu'))
        model.add(K.layers.Dropout(0.3))
        model.add(K.layers.Dense(units=94, activation='relu'))
        model.add(K.layers.Dropout(0.24))
        model.add(K.layers.Dense(units=78, activation='relu'))
        model.add(K.layers.Dropout(0.18))
        model.add(K.layers.Dense(units=62, activation='relu'))
        model.add(K.layers.Dropout(0.12))
        model.add(K.layers.Dense(units=46, activation='relu'))
        model.add(K.layers.Dropout(0.06))
        model.add(K.layers.Dense(units=30, activation='relu'))
        model.add(K.layers.Dropout(0.0))
        model.add(K.layers.Dense(units=21,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    if m==30:
        b_size = 50
        max_epochs = 100
        clear_session()
        model = K.models.Sequential()
        model.add(K.layers.Dense(units=280, input_dim=train_x_zcore.shape[1],  activation='relu'))
        model.add(K.layers.Dropout(0.3))
        model.add(K.layers.Dense(units=153, activation='relu'))
        model.add(K.layers.Dropout(0.15))
        model.add(K.layers.Dense(units=25, activation='relu'))
        model.add(K.layers.Dropout(0.0))
        model.add(K.layers.Dense(units=21,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    if m==35:
        b_size = 100
        max_epochs = 100
        clear_session()
        model = K.models.Sequential()
        model.add(K.layers.Dense(units=200, input_dim=train_x_zcore.shape[1],  activation='relu'))
        model.add(K.layers.Dropout(0.0))
        model.add(K.layers.Dense(units=144, activation='relu'))
        model.add(K.layers.Dropout(0.0))
        model.add(K.layers.Dense(units=87, activation='relu'))
        model.add(K.layers.Dropout(0.0))
        model.add(K.layers.Dense(units=31, activation='relu'))
        model.add(K.layers.Dropout(0.0))
        model.add(K.layers.Dense(units=21,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    if m==40:
        b_size = 80
        max_epochs = 50
        clear_session()
        model = K.models.Sequential()
        model.add(K.layers.Dense(units=360, input_dim=train_x_zcore.shape[1],  activation='relu'))
        model.add(K.layers.Dropout(0.5))
        model.add(K.layers.Dense(units=278, activation='relu'))
        model.add(K.layers.Dropout(0.38))
        model.add(K.layers.Dense(units=195, activation='relu'))
        model.add(K.layers.Dropout(0.26))
        model.add(K.layers.Dense(units=113, activation='relu'))
        model.add(K.layers.Dropout(0.14))
        model.add(K.layers.Dense(units=30, activation='relu'))
        model.add(K.layers.Dropout(0.02))
        model.add(K.layers.Dense(units=21,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    if m==45:
        b_size = 50
        max_epochs = 100
        clear_session()
        model = K.models.Sequential()
        model.add(K.layers.Dense(units=340, input_dim=train_x_zcore.shape[1],  activation='relu'))
        model.add(K.layers.Dropout(0.3))
        model.add(K.layers.Dense(units=185, activation='relu'))
        model.add(K.layers.Dropout(0.15))
        model.add(K.layers.Dense(units=30, activation='relu'))
        model.add(K.layers.Dropout(0.00))
        model.add(K.layers.Dense(units=21,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    if m==50:
        b_size = 50
        max_epochs = 100
        clear_session()
        model = K.models.Sequential()
        model.add(K.layers.Dense(units=340, input_dim=train_x_zcore.shape[1],  activation='relu'))
        model.add(K.layers.Dropout(0.5))
        model.add(K.layers.Dense(units=185, activation='relu'))
        model.add(K.layers.Dropout(0.15))
        model.add(K.layers.Dense(units=30, activation='relu'))
        model.add(K.layers.Dropout(0.00))
        model.add(K.layers.Dense(units=21,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    h = model.fit(train_x_zcore, train_y, batch_size=b_size, epochs=max_epochs, shuffle=True, verbose=1)##调参，节点数，层数
    actual = np.argmax(test_y.values, axis=-1)
    predicted = np.argmax(model.predict(test_x_zcore), axis=-1)
    acc = accuracy_score(actual, predicted)
    recall = recall_score(actual, predicted, average='weighted')
    precision = precision_score(actual,predicted,average='weighted')
    f = open("/public/slst/home/ningwei/TCGA/Methylation450K/feature_importance_6_15/finall_result/"+"RF_0"+"_"+str(m)+".txt",'a') #若文件不存在，系统自动创建。'a'表示可连续写入到文件，保留原内容，在原内容之后写入。可修改该模式（'w+','w','wb'等）
    f.write("acc: "+str(acc)) #将字符串写入文件中
    f.write("\n")   #换行 
    f.write("recall: "+str(recall)) #将字符串写入文件中
    f.write("\n")   #换行 
    f.write("precision: "+str(precision)) #将字符串写入文件中
    f.close()