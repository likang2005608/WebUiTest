#! /usr/bin/env python
# -*- coding: utf-8 -*-
from unittest2 import TestLoader
from case.login_case import TestLogin
import HTMLReport
from utils.create_file import getFileName, getReportNmae
from utils.config import Config

class runTestCase(object):
    """
        运行测试类
    """
    def __init__(self):
        self.file_name=Config().get('report')["file_name"]
        self.report_title=Config().get('report')["report_title"]
        self.description=Config().get("report")["description"]

    def suite(self):
        suite1 = TestLoader().loadTestsFromTestCase(TestLogin)

        # 生成测试报告
        runner = HTMLReport.TestRunner(report_file_name=self.file_name + getReportNmae(),  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                       output_path=getFileName(),  # 保存文件夹名，默认“report”
                                       title=self.report_title,  # 报告标题，默认“测试报告”
                                       description=self.description,  # 报告描述，默认“测试描述”
                                       thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                       thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                                       sequential_execution=True,  # 是否按照套件添加(addTests)顺序执行，
                                       # 会等待一个addTests执行完成，再执行下一个，默认 False
                                       # 如果用例中存在 tearDownClass ，建议设置为True，
                                       # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                       # lang='en'
                                       lang='cn'  # 支持中文与英文，默认中文
                                       )
        # logger().info("测试")
        # logger().debug("测试")
        # logger().warning("测试")
        # logger().error("测试")
        # logger().critical("测试")
        runner.run(suite1)




if __name__ == '__main__':
    runTestCase().suite()