from CV import CV

if  __name__ == '__main__':
    d = r'D:\0COCO\System\桌面\SpeedPan\C++ Primer视频教程（初级中级高级）'
    cv1 = CV(workDir=d, sleepTime=6)
    #speed = 1
    # speed = 1.1
    # speed = 1.2
    #speed = 1.3
    # speed = 1.4
    # speed = 1.5
    #speed = 1.6
    speed = 1.8
    dealOldFilesMode = 0
    gpu = False
    cv1.dealV(speed, dealOldFilesMode, gpu, 8)
    #cv1.dealV(speed = 2, dealOldFilesMode=1)
    #cv1.dealV(speed = 1.8, dealOldFilesMode=1)
    #cv1.dealV(speed = 1.6, dealOldFilesMode = 1)
    #cv1.dealV(speed = 1.5)
    #cv1.dealV(speed = 1.3, dealOldFilesMode = 1)
    #cv1.dealV(speed = 1.2, dealOldFilesMode = 1)
    #cv1.dealV(speed = 1, dealOldFilesMode=1)
    #print(os.getcwd())
    #print(sys.path[0])
    pass