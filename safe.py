from Cryptodome.Cipher import AES
import pickle

AES_BLOCK_SIZE = AES.block_size  # AES 加密数据块大小, 只能是16
AES_KEY_SIZE = 16  # AES 密钥长度（单位字节），可选 16、24、32，对应 128、192、256 位密钥
key = b"v\"JT{cS&j6?g9A=y"


# 待加密文本补齐到 block size 的整数倍
def pad_test(_bytes):
    while len(_bytes) % AES_BLOCK_SIZE != 0:  # 循环直到补齐 AES_BLOCK_SIZE 的倍数
        _bytes += ' '.encode()  # 通过补空格（不影响源文件的可读）来补齐
    return _bytes  # 返回补齐后的字节列表


# AES 加密
def encrypt(_bytes):
    my_cipher = AES.new(key, AES.MODE_ECB)  # 新建一个 AES 算法实例，使用 ECB（电子密码本）模式
    encrypt_data = my_cipher.encrypt(_bytes)  # 调用加密方法，得到加密后的数据
    return encrypt_data  # 返回加密数据


# AES 解密
def decrypt(encrypt_data):
    my_cipher = AES.new(key, AES.MODE_ECB)  # 新建一个 AES 算法实例，使用 ECB（电子密码本）模式
    _bytes = my_cipher.decrypt(encrypt_data)  # 调用解密方法，得到解密后的数据
    return _bytes  # 返回解密数据


def dump(val, path):
    file_content = pickle.dumps(val)
    file_content = pad_test(file_content)
    file_content = encrypt(file_content)
    with open(path, 'wb') as f:
        f.write(file_content)


def load(path):
    with open(path, 'rb') as f:
        file_content = f.read()
    file_content = decrypt(file_content)
    return pickle.loads(file_content)
