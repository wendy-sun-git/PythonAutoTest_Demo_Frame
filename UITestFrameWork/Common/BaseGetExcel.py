import os
from logging import exception
import pandas


class BaseGetExcel:
    def __init__(self, page):
        self.columns = ['元素变量名', '元素名称', '所属页面', '定位方式', '定位值', '超时时间']
        self.page = page

    """
            函数名:read_excels_data(inputdir = '../Cases/')
            功能:读取某目录下的多个excel文件内容
            输入:excel集合目录
            输出:列表:excel中的每一行
        [
            [
        {
            '接口名':'aaa',
            '用例':'用例aaa',
                ……,
            '请求参数':'balabalabala'
        },
        {
            '接口名':'bbb',
            '用例':'用例bbb',
                ……,
            '请求参数':'balabalabala'
        }
    ]
    """

    ## 读取所有文件
    def read_all_excels_data(self, dirs, log):
        dataframe = pandas.DataFrame(self.columns)
        for parents, dirnames, filenames in os.walk(dirs):  # 遍历用例目录下的所有excel文件
            for filename in filenames:  # 依次读取每个文件
                # log.info('filename={}'.format(filename))
                try:
                    datafile = pandas.read_excel(os.path.join(parents, filename))  # 单个excel里面的数据给datafile
                    # log.info("当前正在处理：%s" % filename)  # 打印每一个excel的文件名
                    dataframe = dataframe.append(datafile, ignore_index=True)  # 多个datafile数据按照属性列追加到dataframe
                except exception as e:
                    log.warning("Warning:多excel打开异常，请检查文件格式并确认文件处于关闭状态！,exception={}".format(e))
                    continue
        tolist = dataframe.to_dict(orient="records")  # 按数据列属性为所索引，数据行为值，转换为列表
        return tolist

    ## 读取指定文件
    def get_element_info(self, file_name, var_name):
        try:
            # 单个excel里面的数据给datafile,返回dataframe
            data = pandas.read_excel(file_name, index_col='所属页面')
            data.loc[self.page]
            vars=data[lambda data: data['元素变量名'] == var_name]
            print(vars)
            # log.info("当前正在处理：%s" % filename)  # 打印每一个excel的文件名
            # log.info(data.loc[page_name])
            # return data.loc[self.page].to_dict(orient="records")
            return vars.to_dict(orient="records")
        except exception as e:
            # log.warning("Warning:多excel打开异常，请检查文件格式并确认文件处于关闭状态！,exception={}".format(e))
            pass

    """
    功能：读取目标目录下excel文件名
    函数名：read_excels_names(filepath)
    输入：文件目录
    返回：excel文件名列表
    """

    def read_excels_names(self, filepath):
        for parents, dirnames, filenames in os.walk(filepath):
            return filenames


if __name__ == "__main__":
    bge = BaseGetExcel('login_page')
    pwd = os.getcwd()
    current_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    testdata_path = os.path.join(current_path, 'PageObject')
    testdata_path1 = os.path.join(testdata_path, 'element_info_datas')

    # tolist = bge.read_excels_data(testdata_path, 'ss.log')
    # for item in tolist:
    #     print(item['元素变量名'])

    filename = os.path.join(testdata_path1, 'login_user_password.xlsx')
    print(filename)
    info = bge.get_element_info(filename, 'username_inputbox')
    print(info)
    # print(info['username_inputbox'])

    # print('[0]=%s' % tolist[0])
    # print('[1]=%s' % tolist[1])
    # print('[2]=%s' % tolist[2])
    # print(tolist[0]["元素变量名"])
    # print(tolist[0]["元素名称"])
