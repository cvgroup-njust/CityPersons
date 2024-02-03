from coco import COCO
from eval_MR_multisetup import COCOeval

annType = 'bbox'      #specify type here
print('Running demo for *%s* results.'%(annType))

#initialize COCO ground truth api
annFile = 'E:/cityscapes/CityPersons_annos/test_gt.json'
# initialize COCO detections api
resFile = 'E:/cityscapes/CityPersons_annos/test_dt.json'

## running evaluation
res_file = open("results.txt", "w")
cocoGt = COCO(annFile)
cocoDt = cocoGt.loadRes(resFile)
imgIds = sorted(cocoGt.getImgIds())
cocoEval = COCOeval(cocoGt,cocoDt,annType)
cocoEval.params.imgIds  = imgIds
for id_setup in range(0,4):
    cocoEval.evaluate(id_setup)
    cocoEval.accumulate()
    cocoEval.summarize(id_setup,res_file)

res_file.close()

