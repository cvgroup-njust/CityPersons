# README #

This repo provides bounding box annotations, python evaluation code, and a benchmark for CityPersons, which is a subset of the [Cityscapes dataset](https://www.cityscapes-dataset.com/).
Please download the images from the Cityscapes website!

Welcome to join the competition by submitting your results on the test set!

*You are highly encouraged to use your institutional email account for submission!*

### Benchmark ###

|         Method         | External   training data | MR (Reasonable) | MR (Reasonable_small) | MR (Reasonable_occ=heavy) | MR (All) |
|:----------------------:|:----------------------:|:---------------:|:---------------------:|:-------------------------:|:--------:|
| [APD-pretrain](https://arxiv.org/abs/1910.09188) |  √ |      7.31%     |         10.81%        |           28.07%          |  32.71%  |
| [Pedestron](https://arxiv.org/abs/2003.08799) |  √ |      7.69%     |         9.16%        |           27.08%          |  28.33%  |
| [APD](https://arxiv.org/abs/1910.09188) |  ×  |      8.27%     |         11.03%        |           35.45%          |  35.65%  |
| YT-PedDet |  ×  |      8.41%     |         10.60%        |           37.88%          |  37.22%  |
| STNet |  ×  |      8.92%     |         11.13%        |           34.31%          |  29.54%  |
| [MGAN](https://arxiv.org/abs/1910.06160) |  ×  |      9.29%     |         11.38%        |           40.97%          |  38.86%  |
| DVRNet |  ×  |      10.99%     |         15.68%        |           43.77%          |  41.48%  |
| [HBA-RCNN](https://arxiv.org/abs/1911.11985) |  ×  |      11.26%     |         15.68%        |           39.54%          |  38.77%  |
| [OR-CNN](https://arxiv.org/abs/1807.08407)     |  ×  |      11.32%     |         14.19%        |           51.43%          |  40.19%  |
| [AdaptiveNMS](http://openaccess.thecvf.com/content_CVPR_2019/papers/Liu_Adaptive_NMS_Refining_Pedestrian_Detection_in_a_Crowd_CVPR_2019_paper.pdf)     |  ×  |      11.40%     |         13.64%        |           46.99%          |  38.89%  |
| [Repultion Loss](http://arxiv.org/abs/1711.07752)     |  ×  |      11.48%     |         15.67%        |           52.59%          |  39.17%  |
| [Cascade MS-CNN](https://arxiv.org/abs/1906.09756)     |  ×  |      11.62%     |         13.64%        |           47.14%          |  37.63%  |
| [Adapted FasterRCNN](http://202.119.95.70/cache/12/03/openaccess.thecvf.com/f36bf52f1783160552c75ae3cd300e84/Zhang_CityPersons_A_Diverse_CVPR_2017_paper.pdf)  |  ×  |      12.97%     |         37.24%        |           50.47%          |  43.86%  |
| [MS-CNN](https://arxiv.org/abs/1607.07155)     |  ×  |      13.32%     |         15.86%        |           51.88%          |  39.94%  |

[comment]: <![leaderboard.png](https://bitbucket.org/repo/XXegAKG/images/1374766803-leaderboard.png)> 

Please refer to the [instructions](https://github.com/cvgroup-njust/CityPersons/tree/master/evaluation/?at=default) on submitting results for evaluation.

### What Do We Have? ###

* [Train/val annotations](https://github.com/cvgroup-njust/CityPersons/tree/master/annotations/?at=default)
* [Python evaluation code](https://github.com/cvgroup-njust/CityPersons/tree/master/evaluation/eval_script/?at=default)
* Competition leaderboard for the test set


### Annotation Example ###
![图片1.png](https://github.com/cvgroup-njust/CityPersons/blob/master/imgs/%E5%9B%BE%E7%89%871.png)

### Citation ###

If you use this data and code, please kindly cite the following papers:

```
@INPROCEEDINGS{Shanshan2017CVPR,

  Author = {Shanshan Zhang and Rodrigo Benenson and Bernt Schiele},

  Title = {CityPersons: A Diverse Dataset for Pedestrian Detection},

  Booktitle = {CVPR},

  Year = {2017}
 }

@INPROCEEDINGS{Cordts2016Cityscapes,

title={The Cityscapes Dataset for Semantic Urban Scene Understanding},

author={Cordts, Marius and Omran, Mohamed and Ramos, Sebastian and Rehfeld, Timo and Enzweiler, Markus and Benenson, Rodrigo and Franke, Uwe and Roth, Stefan and Schiele, Bernt},

booktitle={Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},

year={2016}
}
```
---------------------------------------------------------------------------------------------------------------------
This material is presented to ensure timely dissemination of scholarly and technical work. Copyright and all rights therein are retained by authors or by other copyright holders. All persons copying this information are expected to adhere to the terms and constraints invoked by each author’s copyright. In most cases, these works may not be reposted without the explicit permission of the copyright holder.
