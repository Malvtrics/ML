+ NLP = NLU(understanding) + NLG(generating)

+ 场景：文本分类 、相似度计算、问答、摘要
+ 历史： 1950年代 基于人工构建的规则 1970年代 基于统计语言学 2003年 神经网络语言模型 seq2seq encoder->context->decoder

+ 最大熵和CRF
+ 实际情况下计算量很大，近几年用的频率不高
+ CRF one case:
+ https://legacy.gitbook.com/book/csrgxtu/-basketball-prediction-based-on-crf/details 

+ 最大熵理论：在满足当前的约束条件下，其他的所有可能不做假设
+ 字面意思：最大熵原理指出，当我们需要对一个随机事件的概率分布进行预测时，我们的预测应当满足全部已知的条件，而对未知的情况不要做任何主观假设。 
（不做主观假设这点很重要。） 在这种情况下，概率分布最均匀，预测的风险最小。 因为这时概率分布的信息熵最大，所以人们称这种模型叫“最大熵模型”。

+ 但是实际应用中计算量太大，所以没有人采用
+ 刚开始也只有IBM 这种有计算能力的公司用
 
+ 最后研究人员找到了几个最适合用最大熵模型的场景：计算量相对不是很大的自然语言处理问题 比如词性标注和句法分析
+ 成功将上下文信息、词性、句子成分通过最大熵模型结合起来做出了当时世界上最好的词性标识系统和句法分析器

+ 但是最大熵模型的计算量依然是个拦路虎

+ build a CRF to tag for a sentence:
+ feature functions in CRF:
+ input: 
+ a sentence-> s
+ current location of the tag->i
+ 当前词和前一个词的标签
+ output:0 or 1
+ note:通过限制我们的特征只依赖于当前与之前的词的标签，而不是句子中的任意标签，实际上我建立了一种特殊的线性CRF：
+ 例如某个特征函数就可以用来衡量当上一个词是very是，当前词有多少程度会被标记为一个形容词
 
