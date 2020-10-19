import tagui as t
import os
import PIL.Image as im
import logging

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

t.close()

logging.basicConfig(filename = "log.txt")
srcDirectory = "OrgImage"
t.init(visual_automation = True)


for target in findAllFile(srcDirectory):
    target_image = 'OrgImage/' + target
    t.url('https://www.bing.com')
    t.click('//div[@id="sb_sbi"]/img')
    t.upload("input.fileinput",target_image)
    t.wait(3)

    succDownload = False

    image_nums = t.count('//a[@class="richImgLnk"]')
    print(image_nums)

    if t.click('//li[contains(string(),"Pages")]') == False:
        image_nums = 0
    t.wait(3)


    for i in range(1, image_nums):
        if t.click(f'(//a[@class="richImgLnk"])[{i}]'):

            t.wait(3)
            t.keyboard('[ctrl]l')
            t.keyboard('[ctrl]c')
            imgUrl = t.clipboard()
            print(imgUrl)
            tarNoExtension = target.split('.')[0]
            if t.download(imgUrl,'HDImage/' + tarNoExtension):
                a=im.open('HDImage/' + tarNoExtension)
                a.save('HDImage/' + target)
                succDownload = True
                t.keyboard('[ctrl]w')
                break
            
            t.keyboard('[ctrl]w')


    if succDownload:
        print("Image " + target + " scraped succ")
        logging.log(logging.INFO, "Image " + target + " scraped succ")
    else:
        print("Image " + target + " scraped fail")
        logging.log(logging.ERROR, "Image " + target + " scraped fail")



t.close()
