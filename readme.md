# 排序算法

## 归并排序

没太搞懂，回头再继续研究一下，脑子一团浆糊

## 线性排序

1. 线性排序算法包括桶排序、计数排序、基数排序。
 
2. 线性排序算法的时间复杂度为O(n)。
 
3. 此3种排序算法都不涉及元素之间的比较操作，是非基于比较的排序算法。
 
4. 对排序数据的要求很苛刻，重点掌握此3种排序算法的适用场景

### 桶排序

#### 算法原理
- 分成有序桶：将要排序的数据分到几个有序的桶里
- 桶内快排：每个桶里的数据再单独进行快速排序。
- 按桶序取出：桶内排完序之后，再把每个桶里的数据按照顺序依次取出，组成的序列就是有序的了。

#### 使用条件
- 要排序的数据需要很容易就能划分成m个桶，并且桶与桶之间有着天然的大小顺序。
- 数据在各个桶之间分布是均匀的。

#### 适用场景
- 桶排序比较适合用在**外部排序**中
> 外部排序就是数据存储在外部磁盘且数据量大，但内存有限无法将整个数据全部加载到内存中。

#### 应用案例

1）需求描述：

有10GB的订单数据，需按订单金额（假设金额都是正整数）进行排序
但内存有限，仅几百MB

2）解决思路：

扫描一遍文件，看订单金额所处数据范围，比如1元-10万元，那么就分100个桶。
第一个桶存储金额1-1000元之内的订单，第二个桶存1001-2000元之内的订单，依次类推。
每个桶对应一个文件，并按照金额范围的大小顺序编号命名（00，01，02，…，99）。
将100个小文件依次放入内存并用快排排序。
所有文件排好序后，只需按照文件编号从小到大依次读取每个小文件并写到大文件中即可。

3）注意点：若单个文件无法全部载入内存，则针对该文件继续按照前面的思路进行处理即可。

### 计数排序

#### 算法原理
- 分桶：当要排序的n个数据所处范围并不大时，比如最大值为k，则分成k个桶，O(n)
- 每个桶内的数据值都是相同的，就省掉了桶内排序的时间。
- 排序：通过桶计数后获得最终的排序后数组

#### 使用条件
- 只能用在数据范围不大的场景中，若数据范围k比要排序的数据n大很多，就不适合用计数排序；
    > 因为是使用空间换时间的方式,空间是有限的
- 计数排序只能给非负整数排序，其他类型需要在不改变相对大小情况下，转换为非负整数；
    > 因为数组下标不能为负数
    >
    > 比如如果考试成绩精确到小数后一位，就需要将所有分数乘以10，转换为整数。

#### 应用案例
1）需求描述：

假设有 8 个考生，分数在 0 到 5 分之间。这 8 个考生的成绩我们放在一个数组 A[8] 中，
A = [2, 5, 3, 0, 2, 3, 0, 3]

2）解决思路：

1. 考生的成绩从 0 到 5 分，我们使用大小为 6 的数组 C[6] 表示桶，其中下标对应分数
2. 遍历一遍数组A，分别放到 C 中，得到最终的数组 C = [2, 0, 2, 3, 0, 1]
3. 对C进行顺序求和，C = [2, 2, 4, 7, 7, 8]
4. 声明一个X位的数组R存放最终的有序数组。遍历A，通过C的值依次插入R，即得到最终有序的R数组
```python
R = ["", "", "", "", "", "", "", ""]
A = [2, 5, 3, 0, 2, 3, 0, 3]
C = [2, 2, 4, 7, 7, 8]

for i in A:
    R_index = C[i] - 1
    R[R_index] = i
    C[i] = C[i] - 1
print(R)
``` 


### 基数排序
#### 算法原理（以排序10万个手机号为例来说明）
- 将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零。
- 然后，从最低位开始，依次进行一次排序。这样从最低位排序一直到最高位排序完成以后, 数列就变成一个有序序列。
    > 比如:比较两个手机号码a，b的大小，如果在前面几位中a已经比b大了，那后面几位就不用看了。
     借助稳定排序算法的思想，可以先按照最后一位来排序手机号码，然后再按照倒数第二位来重新排序，以此类推，最后按照第一个位重新排序。
     经过11次排序后，手机号码就变为有序的了。
     每次排序有序数据范围较小，可以使用桶排序或计数排序来完成。

#### 使用条件
- 要求数据可以分割独立的“位”来比较；
- 位之间由递进关系，如果a数据的高位比b数据大，那么剩下的地位就不用比较了；
- 每一位的数据范围不能太大，要可以用线性排序，否则基数排序的时间复杂度无法做到O(n)。

## 堆排序
### 堆
> - 堆是一个完全二叉树。
> - 堆中的每个节点的值都必须大于等于或者小于等于其子树中的每个节点的值。

### 为什么快速排序要比堆排序性能好？
- 堆排序的数据访问方式没有快速排序友好，因为他不连续，这样对cpu不友好
- 同样的数据，堆排序的数据交换次数大于快速排序

## 排序总结

|         | 时间复杂度        | 是否稳定排序 | 是否原地排序 |
| :---:   | :---:            | :---:      | :---:      |
| 冒泡排序 | O(n²)            | ✔          | ✔          |
| 插入排序 | O(n²)            | ✔          | ✔          |
| 选择排序 | O(n²)            | ✘          | ✔          |
| 快速排序 | O(nlogn)         | ✘          | ✔          |
| 归并排序 | O(nlogn)         | ✔          | ✘          |
| 计数排序 | O(n+k)k是数据范围  | ✔         | ✘          |
| 桶排序   | O(n)             | ✔          | ✘          |
| 基数排序 | O(dn)d是维度      | ✔          | ✘          |
| 堆排序   | O(nlogn)         | ✘          | ✔          |

# 查找算法

## 二分查找
  > 二分查找针对的是一个有序的数据集合，每次通过跟区间中间的元素对比，
  将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间缩小为0
  
### 优点
- 时间复杂度低: O(logn)
- 省内存(对比散列表,二叉树)

### 使用条件
- 二分查找依赖的是顺序表结构，即**数组**。
- 二分查找针对的是有序数据，因此只能用在插入、删除操作不频繁，**一次排序多次查找**的场景中。
- **数据量太小**不适合二分查找，与直接遍历相比效率提升不明显。
    > 但有一个例外，就是数据之间的比较操作非常费时，比如数组中存储的都是
    长度超过300的字符串，那这是还是尽量减少比较操作使用二分查找吧。
- **数据量太大**也不是适合用二分查找，因为数组需要连续的空间，若数据量太大，往往找不到存储如此大规模数据的连续内存空间。

# 散列表

## 散列表的由来?
- 散列表来源于数组，它借助散列函数对数组这种数据结构进行扩展，利用的是数组支持按照下标随机访问元素的特性

## 如何设计这样一个散列表呢？
- 设计一个合适的散列函数
>1.要尽可能让散列后的值随机且均匀分布，这样会尽可能减少散列冲突，即便冲突之后，分配到每个槽内的数据也比较均匀。
>
>2.除此之外，散列函数的设计也不能太复杂，太复杂就会太耗时间，也会影响到散列表的性能。
>
> 3.常见的散列函数设计方法：直接寻址法、平方取中法、折叠法、随机数法等。
- 定义装载因子阈值，并且设计动态扩容策略
>1.如何设置装载因子阈值？
> 
> ①可以通过设置装载因子的阈值来控制是扩容还是缩容，支持动态扩容的散列表，插入数据的时间复杂度使用摊还分析法。
> 
> ②装载因子的阈值设置需要权衡时间复杂度和空间复杂度。如何权衡？如果内存空间不紧张，对执行效率要求很高，可以降低装载因子的阈值；相反，如果内存空间紧张，对执行效率要求又不高，可以增加装载因子的阈值。
> 
> 2.如何避免低效扩容？分批扩容
> 
> ①分批扩容的插入操作：当有新数据要插入时，我们将数据插入新的散列表，并且从老的散列表中拿出一个数据放入新散列表。每次插入都重复上面的过程。这样插入操作就变得很快了。
> 
> ②分批扩容的查询操作：先查新散列表，再查老散列表。
> 
> ③通过分批扩容的方式，任何情况下，插入一个数据的时间复杂度都是O(1)。
>
>
- 合适的散列冲突解决方法
> ①常见的2种方法：开放寻址法和链表法。
> 
> ②大部分情况下，链表法更加普适。而且，我们还可以通过将链表法中的链表改造成其他动态查找数据结构，比如红黑树、跳表，来避免散列表时间复杂度退化成O(n)，抵御散列冲突攻击。
> 
> ③但是，对于小规模数据、装载因子不高的散列表，比较适合用开放寻址法。

## 为什么散列表和链表经常放在一起使用？
- 散列表的优点：支持高效的数据插入、删除和查找操作
- 散列表的缺点：不支持快速顺序遍历散列表中的数据
- 如何按照顺序快速遍历散列表的数据？只能将数据转移到数组，然后排序，最后再遍历数据。
- 我们知道散列表是动态的数据结构，需要频繁的插入和删除数据，那么每次顺序遍历之前都需要先排序，这势必会造成效率非常低下。
- 如何解决上面的问题呢？就是将散列表和链表（或跳表）结合起来使用。
> 散列表和链表、跳表的混合使用，是为了结合数组和链表的优势，规避它们的不足

## 散列表和链表的结合使用实例
1. 缓存淘汰算法(LRU)
2. LinkedHashMap
3. redis的有序集合

# 哈希算法

## 常见应用
- 安全加密
- 唯一标识
- 数据校验
- 散列函数
- 负载均衡
- 数据分片
- 分布式存储

# 二叉树
## 树的常用概念
- 节点：树中的每个元素称为节点
- 父子关系：相邻两节点的连线，称为父子关系
- 根节点：没有父节点的节点
- 叶子节点：没有子节点的节点
- 父节点：指向子节点的节点
- 子节点：被父节点指向的节点
- 兄弟节点：具有相同父节点的多个节点称为兄弟节点关系
- 节点的高度：节点到叶子节点的最长路径所包含的边数
- 节点的深度：根节点到节点的路径所包含的边数
- 节点的层数：节点的深度+1（根节点的层数是1）
- 树的高度：等于根节点的高度

## 特殊的二叉树
- 满二叉树
- 完全二叉树

## 二叉树的存储方式
- 链式存储(大部分)
- 顺序存储(完全二叉树)

## 二叉树的遍历
1. 前序遍历：对于树中的任意节点来说，先打印这个节点，然后再打印它的左子树，最后打印它的右子树。
2. 中序遍历：对于树中的任意节点来说，先打印它的左子树，然后再打印它的本身，最后打印它的右子树。
3. 后序遍历：对于树中的任意节点来说，先打印它的左子树，然后再打印它的右子树，最后打印它本身。

> 时间复杂度: O(n)

## 平衡二叉搜索树
> 二叉树中任意一个节点的左右子树的高度相差不大于1.

### 红黑树（近似平衡）

#### 特性
- 根节点是黑色的
- 每个叶子节点都是黑色的空节点（NIL），也就是说，叶子节点不存储数据
- 任何相邻的节点都不能同时为红色，也就是说，红色节点是被黑色节点隔开
- 每个节点，从该节点到达其可达叶子节点的所有路径，都包含相同数目的黑色节点

#### 适用的场景
动态插入、删除、查找数据的场景

#### 解决的问题
解决普通二叉查找树在数据更新的过程中，复杂度退化的问题而产生
红黑树的高度近似 log2n，所以它是近似平衡，插入、删除、查找操作的时间复杂度都是 O(logn)。
