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
for year in ['2007', '2012']:
  for split in ['train', 'val', 'trainval', 'test']:
    name = 'voc_{}_{}'.format(year, split)
    __sets[name] = (lambda split=split, year=year: pascal_voc(split, year))
#__sets是一个字典，根据名字生成一个匿名函数

def get_imdb(name):
  """Get an imdb (image database) by name."""
  if name not in __sets:
    raise KeyError('Unknown dataset: {}'.format(name))
  return __sets[name]()
    
    
    
    
    
    
    
    
