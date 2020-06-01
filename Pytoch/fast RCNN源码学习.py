加载数据集的时候比较复杂
在trainval_net.py文件中主要通过下面一段去加载

imdb, roidb, ratio_list, ratio_index = combined_roidb(args.imdb_name)
sampler_batch = sampler(train_size, args.batch_size)
dataset = roibatchLoader(roidb, ratio_list, ratio_index, args.batch_size, imdb.num_classes, training=True)
#sampler (Sampler, optional) – defines the strategy to draw samples from the dataset. If specified, shuffle must be False.
dataloader = torch.utils.data.DataLoader(dataset, batch_size=args.batch_size,sampler=sampler_batch, num_workers=args.num_workers)

#这里的roibatchLoader方法是从roi_data_layer这个模块来的
from roi_data_layer.roidb import combined_roidb
from roi_data_layer.roibatchLoader import roibatchLoader

#这个roibatchLoader继承了pytorch自己dataset
class roibatchLoader(data.Dataset):
  def __init__(self, roidb, ratio_list, ratio_index, batch_size, num_classes, training=True, normalize=None):
    # 构造函数里面做了这么一件事 given the ratio_list, we want to make the ratio same for each batch.
    # ratio_list 来自 roi_data_layer 的 combined_roidb 中的rank_roidb_ratio 方法
 
ratio_list, ratio_index = rank_roidb_ratio(roidb)

datasets.factory 中 
for year in ['2014']:
  for split in ['train', 'val', 'capval', 'valminuscapval', 'trainval']:
    name = 'coco_{}_{}'.format(year, split)
    __sets[name] = (lambda split=split, year=year: coco(split, year))
#__sets是一个字典，根据名字生成一个匿名函数，有两个参数split和year，冒号后面表示要执行的函数

def get_imdb(name):
  """Get an imdb (image database) by name."""
  if name not in __sets:
    raise KeyError('Unknown dataset: {}'.format(name))
  return __sets[name]() #coco('train','2014')
    
#coco.py 继承了imdb
from datasets.imdb import imdb
class coco(imdb):
  def __init__(self, image_set, year):
    imdb.__init__(self, 'coco_' + year + '_' + image_set)
    #后面就是如何加载coco数据集
    self._data_path = osp.join(cfg.DATA_DIR, 'coco')
    #在model/utils/config.py中可以看到DATA_DIR的定义
    # Root directory of project
    #__C.ROOT_DIR = osp.abspath(osp.join(osp.dirname(__file__), '..', '..', '..'))
    #可以看出当时作者是把coco数据放在工程目录中训练的
    self._COCO = COCO(self._get_ann_file()) #这一步用了coco自己的API，里面是自己的函数，拿到标注json文件路径
    
  def _get_ann_file(self):
      prefix = 'instances' if self._image_set.find('test') == -1 \ #太长的代码为了增强可读性，可以打斜杠到下一行去写
      else 'image_info'
      return osp.join(self._data_path, 'annotations',
                  prefix + '_' + self._image_set + self._year + '.json')
    # COCO API
    #from pycocotools.coco import COCO
    #下面的链接是pycocotools API的github地址，学习一下构造函数
    #https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/coco.py
    
    class COCO:
      def __init__(self, annotation_file=None):
          self.dataset,self.anns,self.cats,self.imgs = dict(),dict(),dict(),dict()  #dict的另外一种定义方式
          self.imgToAnns, self.catToImgs = defaultdict(list), defaultdict(list)
          #这里我们看到用了defaultdict为啥呢？？很有趣 defaultdict是dict的一个子类，重写了__missing__方法和增加了default_factory属性
          #defaultfactory可以是list（可以用append），看可以是int（可以用来计数）等等比dict简单快速，复习的话可以看下面链接
          #https://docs.python.org/3/library/collections.html#collections.defaultdict
          #顺便看了下dict 发现一个有趣的知识点字典的比较，后面注意一下
          #An equality comparison between one dict.values() view and another will always return False. 
          #This also applies when comparing dict.values() to itself:
          if not annotation_file == None:
              print('loading annotations into memory...')
              tic = time.time()
              dataset = json.load(open(annotation_file, 'r'))
              #第一次看到了assert的用法，工程中的使用，应该很有用
              assert type(dataset)==dict, 'annotation file format {} not supported'.format(type(dataset))
              print('Done (t={:0.2f}s)'.format(time.time()- tic))  #如何打印程序的执行时间
              self.dataset = dataset
              self.createIndex()
              
我们回到coco.py 接本文46行
  cats = self._COCO.loadCats(self._COCO.getCatIds())
  self._classes = tuple(['__background__'] + [c['name'] for c in cats]) 
  #加一个背景类 知识点：数组可以用加号直接扩展，这里用tuple 类型其实是一种强调，因为tuple元素不能修改，所以强调分类数目是极其确定的
  
  self._class_to_ind = dict(list(zip(self.classes, list(range(self.num_classes)))))
  self._class_to_coco_cat_id = dict(list(zip([c['name'] for c in cats], self._COCO.getCatIds()))) 
  #python3中使用

    
    
    
