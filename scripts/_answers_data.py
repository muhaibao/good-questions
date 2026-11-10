# -*- coding: utf-8 -*-
"""Verified answers for published questions. Sources checked separately."""

ANSWERS = {}

ANSWERS["2026-11-09-ai-explainable"] = {
  "summary": "「可解释人工智能」（XAI）的主流理由是：当模型用于信贷、医疗、刑事司法等高风险决策时，仅有预测准确率不够，还需要让相关人理解、质疑并追责。与此同时，学界对「解释」本身能否可靠存在尖锐分歧：有人主张发展事后解释技术，有人认为对黑箱做事后说明往往不忠实，高风险场景应直接使用本身可解释的模型。",
  "views": [
    {
      "position": "高风险决策必须可解释、可追责",
      "holders": "政策圈与部分机器学习研究者（如 Finale Doshi-Velez、Been Kim 等倡导把可解释性当作一门可检验的科学）",
      "argument": "若模型影响人的权利与安全，使用者与受影响者需要知道依据是什么，才能发现数据偏差、满足监管并建立有限的信任。可解释性应被当作可定义、可评估的目标，而不是口号。",
      "sources": [
        {"title": "Doshi-Velez & Kim, Towards A Rigorous Science of Interpretable Machine Learning (arXiv:1702.08608)", "url": "https://arxiv.org/abs/1702.08608"},
      ],
    },
    {
      "position": "事后解释不可靠，高风险场景应使用本质可解释模型",
      "holders": "Cynthia Rudin",
      "argument": "对黑箱模型再套一层「解释器」，解释可能与模型真实机制不一致，反而造成虚假安全感。在医疗、刑事司法等后果严重的领域，应优先设计本身可解读的模型，而不是先上黑箱再补解释。",
      "sources": [
        {"title": "Rudin, Stop explaining black box machine learning models for high stakes decisions…（PMC 开放版本）", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9122117/"},
      ],
    },
    {
      "position": "「可解释」一词本身含混，目标需要先澄清",
      "holders": "Zachary Lipton",
      "argument": "人们把可解释性用来指透明度、可模拟性、事后理由或因果洞察等不同东西；不清楚要解决哪种需求，就无法判断一种方法是否成功。先区分问题，再谈技术。",
      "sources": [
        {"title": "Lipton, The Mythos of Model Interpretability (arXiv:1606.03490)", "url": "https://arxiv.org/abs/1606.03490"},
      ],
    },
  ],
  "open_parts": "仍然没有公认的「解释质量」尺度：对谁解释、解释到哪一层算够、解释与隐私或商业秘密如何权衡，都未解决。本质可解释模型在大规模深度网络上能否达到与黑箱相当的性能，也仍在争论。",
}

ANSWERS["2026-11-09-ai-fooled"] = {
  "summary": "深度网络（以及许多其他分类器）会把对人眼几乎不可见的扰动判成完全不同的类别，这类「对抗样本」自 2013 年起被系统揭示。一个有影响力的解释是：高维空间里线性决策边界很容易被小扰动推过；也有研究主张，对抗样本反映的是数据中对人类不显著、对模型却有用的特征，而不只是训练缺陷。",
  "views": [
    {
      "position": "这是深度网络在高维输入上的结构性脆弱",
      "holders": "Szegedy 等人首先系统报告该现象；Goodfellow、Shlens 与 Szegedy 提出线性解释",
      "argument": "即使网络在测试集上准确率很高，仍存在精心构造的微小扰动导致高置信度误判。一个简洁解释是：在高维空间中，沿权重方向累积的微小变化足以越过决策边界，因此「看起来稳健」与「对定向扰动稳健」不是一回事。",
      "sources": [
        {"title": "Szegedy et al., Intriguing properties of neural networks (arXiv:1312.6199)", "url": "https://arxiv.org/abs/1312.6199"},
        {"title": "Goodfellow, Shlens & Szegedy, Explaining and Harnessing Adversarial Examples (arXiv:1412.6572)", "url": "https://arxiv.org/abs/1412.6572"},
      ],
    },
    {
      "position": "网络会被对人无意义的图像「高置信度识别」",
      "holders": "Nguyen、Yosinski 与 Clune",
      "argument": "用进化算法生成的对人类完全不像目标物体的图像，仍可被深度网络以高置信度分类，说明模型抓到的判别依据不必与人类的形状、语义一致。",
      "sources": [
        {"title": "Nguyen, Yosinski & Clune, Deep Neural Networks are Easily Fooled (arXiv:1412.1897)", "url": "https://arxiv.org/abs/1412.1897"},
      ],
    },
    {
      "position": "对抗样本未必是「漏洞」，也可能是有用特征",
      "holders": "Ilyas 等（2019）",
      "argument": "有研究显示，对抗扰动可能对应数据中真实存在、对分类有统计预测力、但人类不使用的特征；因此「愚弄」不完全等于模型瞎猜，也提出了与人类感知对齐的问题。",
      "sources": [
        {"title": "Ilyas et al., Adversarial Examples Are Not Bugs, They Are Features (arXiv:1905.02175)", "url": "https://arxiv.org/abs/1905.02175"},
      ],
    },
  ],
  "open_parts": "目前没有任何被广泛接受的训练方法能在保持性能的同时消除对抗脆弱性。对抗样本究竟主要是线性几何、非稳健特征，还是分布外泛化失败，仍无定论；它们对现实物理世界攻击的普遍程度也还在研究中。",
}

ANSWERS["2026-11-09-biz-cost-disease"] = {
  "summary": "医疗、教育等劳动密集型服务的实际价格长期上升，而电子产品等可贸易商品则大幅降价。一个经典解释是鲍莫尔成本病：生产率难提升的部门必须跟上高生产率部门的工资，于是相对价格上升。也有人强调监管、土地与住房成本、以及质量改进未被价格指数充分计量。Patrick Collison 把这个问题列为进步研究的核心疑问之一。",
  "views": [
    {
      "position": "鲍莫尔成本病：生产率不对称推高相对价格",
      "holders": "William J. Baumol（1967）；Eric Helland 与 Alexander Tabarrok 以此解释美医疗和教育价格",
      "argument": "若某部门难以用机器替代人力（如课堂教学、护理），而整个经济的工资被高生产率部门拉高，这些「停滞部门」的单位成本就会相对上升。这不一定意味着浪费，而可能是结构现象。",
      "sources": [
        {"title": "Baumol, Macroeconomics of Unbalanced Growth（JSTOR 条目）", "url": "https://www.jstor.org/stable/1812671"},
        {"title": "Helland & Tabarrok, Why Are the Prices So Damn High?（Mercatus，Internet Archive 存档）", "url": "https://web.archive.org/web/2020/https://www.mercatus.org/research/books/why-are-prices-so-damn-high"},
        {"title": "Wikipedia：Baumol's cost disease", "url": "https://en.wikipedia.org/wiki/Baumol%27s_cost_disease"},
      ],
    },
    {
      "position": "价格变化中有很大一块是质量与范围未被测准",
      "holders": "价格统计与健康经济学家中的常见立场；Collison 在问题中亦明确提出这一可能",
      "argument": "今天的医疗能治疗更多疾病、教育年限与服务内容也已变化。若价格指数没有充分纳入质量改进，就会把「更好」读成「更贵」。要回答「为什么贵」，必须先分清数量、质量与纯价格。",
      "sources": [
        {"title": "Patrick Collison, Questions（含对该问题的表述）", "url": "https://patrickcollison.com/questions"},
      ],
    },
    {
      "position": "供给约束与制度成本同样重要",
      "holders": "关注住房、职业许可与行政负担的研究者与评论者（Collison 引用的 AEI/BLS 价格对照图常被用来展示部门差异）",
      "argument": "若土地、许可、保险和合规成本上升，服务价格也会被推高，这与纯鲍莫尔机制可以并存。部门之间的价格分化本身，可见于基于官方统计的长期对照图。",
      "sources": [
        {"title": "AEI：Chart of the day (or century)（BLS 数据整理的长期价格对照）", "url": "https://www.aei.org/economics/chart-of-the-day-or-century/"},
      ],
    },
  ],
  "open_parts": "在医疗或高等教育的涨价中，成本病、质量改进、市场势力和监管各占多少，没有公认分解。跨国差异也提示制度很重要，但要把「该改哪一条制度」说成因果结论，证据仍然不足。",
}

ANSWERS["2026-11-09-sci-pnp"] = {
  "summary": "P 对 NP 问的是：凡是「答案可在多项式时间内验证」的问题，是否也能在多项式时间内求解。绝大多数复杂性理论研究者相信 P ≠ NP，但既没有证明，也没有被广泛接受的否定证明框架。它是克莱数学研究所七个千禧年难题之一。",
  "views": [
    {
      "position": "P ≠ NP（主流猜想）",
      "holders": "绝大多数复杂性理论学者的工作假设；Clay 官方命题陈述以此为开放问题",
      "argument": "若 P = NP，则大量搜索、优化与定理证明问题将变得高效可解，现有的许多密码学假设也会动摇。经验上，人们找不到对 NP 完全问题的通用高效算法，这被当作支持不等的间接理由，但它不是证明。",
      "sources": [
        {"title": "Clay Mathematics Institute：P vs NP", "url": "https://www.claymath.org/millennium/p-vs-np/"},
      ],
    },
    {
      "position": "我们可能尚不具备解决问题所需的数学工具",
      "holders": "Scott Aaronson 在综述中系统讨论了已知障碍（如相对论化、自然证明等）",
      "argument": "一系列「障碍」结果表明，许多一度看起来有希望的证明策略，在形式上无法区分 P 与 NP。因此，即便猜想为真，证明也可能要求全新的想法，而不是把现有技术再推进一步。",
      "sources": [
        {"title": "Aaronson, P ≟ NP（综述文稿 PDF）", "url": "https://www.scottaaronson.com/papers/pnp.pdf"},
      ],
    },
  ],
  "open_parts": "问题仍完全开放：既没有 P = NP 的构造性证明，也没有 P ≠ NP 的不可逆论证。即使将来证明了不等，具体哪些自然问题处于中间地带、近似与平均情况复杂度如何，也还会留下大量未解细节。",
}

ANSWERS["2026-11-09-phil-math"] = {
  "summary": "这是数学哲学的核心分歧之一。柏拉图主义（或实在论）认为数学对象独立于人类心灵而存在，数学家是在发现真理；经验论、形式主义与唯名论的不同变种则认为数学是人类发明的符号系统、约定或结构描述。双方都能解释数学的部分特征，但在「为何数学对自然科学如此有效」上持续交锋。",
  "views": [
    {
      "position": "数学是被发现的（柏拉图主义 / 实在论）",
      "holders": "传统上与柏拉图、以及现代数学实在论者相关；斯坦福哲学百科对此有系统综述",
      "argument": "数学命题似乎具有客观真假：即使没有人想过某条定理，它也真或假。不同文明独立得到相近的数论与几何结果，也被用作「不是任意约定」的直观证据。",
      "sources": [
        {"title": "Stanford Encyclopedia of Philosophy：Platonism in the Philosophy of Mathematics", "url": "https://plato.stanford.edu/entries/platonism-mathematics/"},
        {"title": "Stanford Encyclopedia of Philosophy：Philosophy of Mathematics", "url": "https://plato.stanford.edu/entries/philosophy-mathematics/"},
      ],
    },
    {
      "position": "数学是被发明的（唯名论 / 形式主义等）",
      "holders": "唯名论与各种反实在论立场，SEP《数学唯名论》条目有梳理",
      "argument": "我们看不到抽象的「数」或「集合」，只能看到符号、规则与人类实践。数学对象若不存在于时空之中，其认识如何可能，是实在论必须回答的难题；发明论则把数学看作被构造出来的语言。",
      "sources": [
        {"title": "Stanford Encyclopedia of Philosophy：Nominalism in the Philosophy of Mathematics", "url": "https://plato.stanford.edu/entries/nominalism-mathematics/"},
      ],
    },
    {
      "position": "无论发明还是发现，其「不合理的有效性」仍需解释",
      "holders": "Eugene Wigner（1960）",
      "argument": "Wigner 指出，为纯数学理由发展出的结构，后来常在物理学中精确适用，这件事本身令人惊讶。它并不直接裁决发明/发现之争，但要求任何一方都必须说明：数学与世界为何贴合得如此好。",
      "sources": [
        {"title": "Wigner, The Unreasonable Effectiveness of Mathematics in the Natural Sciences（PDF）", "url": "https://www.maths.ed.ac.uk/~v1ranick/papers/wigner.pdf"},
        {"title": "Wikipedia 对该文的条目", "url": "https://en.wikipedia.org/wiki/The_Unreasonable_Effectiveness_of_Mathematics_in_the_Natural_Sciences"},
      ],
    },
  ],
  "open_parts": "没有实验可以一锤定音。结构主义等中间立场试图回避「抽象对象是否存在」，但关于数学真理的客观性、以及有效性从何而来，仍是开放的哲学问题。",
}

ANSWERS["2026-11-09-psych-incubation"] = {
  "summary": "心理学把「放下问题后突然想通」称为孵化效应。元分析显示，在适当条件下，中断并插入其他活动对问题解决有小到中等的帮助，尤其是发散性任务。解释主要有两类：一是休息降低了错误思路的固着，二是思维漫游或无意识加工继续工作。效应存在，但机制与可预期的大小仍有争议。",
  "views": [
    {
      "position": "孵化是真实的、可测量的小组效应",
      "holders": "Sio 与 Ormerod（2009）的元分析",
      "argument": "综合大量实验后，平均孵化效应为正（约小到中等），在发散思维任务上更明显；准备时间更长时效应更大，孵化阶段若插入高负荷任务则会削弱效果。因此「出去走走再想」并非纯传说。",
      "sources": [
        {"title": "Sio & Ormerod, Does incubation enhance problem solving? A meta-analytic review（PubMed）", "url": "https://pubmed.ncbi.nlm.nih.gov/19210055/"},
        {"title": "Wikipedia：Incubation (psychology)", "url": "https://en.wikipedia.org/wiki/Incubation_(psychology)"},
      ],
    },
    {
      "position": "低要求的走神有助于创造性孵化",
      "holders": "Baird、Smallwood、Schooler 等（2012）",
      "argument": "一项实验发现，在孵化阶段做低要求任务（比休息或高要求任务更有利于先前遇到的非常规用途问题），且受益与思维漫游增多有关。这意味着「轻度分心」可能比死死盯着问题或完全发呆更有用。",
      "sources": [
        {"title": "Baird et al., Inspired by distraction（PubMed）", "url": "https://pubmed.ncbi.nlm.nih.gov/22941876/"},
      ],
    },
  ],
  "open_parts": "孵化何时有效、对哪些题型有效，仍不稳定；实验室效应能否推广到真实工作中的「顿悟」，证据有限。无意识继续加工、遗忘固着、还是单纯的注意重置，机制尚未分清。",
}

ANSWERS["2026-11-09-ai-bubble"] = {
  "summary": "这是一道混合了价值判断与周期判断的问题：有人把估值回调看作对过度承诺的纠正而感到宽慰，有人认为把「能力进展」与「金融资产价格」混为一谈会误判趋势。较审慎的研究提醒：即便模型能力提升，宏观经济与就业的转变也可能慢于叙事。题本身没有唯一正确答案，关键是把金融泡沫、技术现实和社会影响分开讨论。",
  "views": [
    {
      "position": "若价格远超可验证的回报，回调未必是坏事",
      "holders": "该 Ask HN 帖中持「泡沫该破」立场的讨论者；经济史上对投机过热的一般分析",
      "argument": "当投资、招聘与宣传以尚未实现的利润为前提时，资源会被错误配置。价格回落可以让资本与注意力回到有真实需求的地方。是否「庆幸」，取决于你是否把纠正浪费视为好事，而不是取决于模型是否突然变得无用。",
      "sources": [
        {"title": "Ask HN 原帖及讨论：As a human, are you glad the AI bubble is bursting?", "url": "https://news.ycombinator.com/item?id=50421778"},
        {"title": "Wikipedia：Technological unemployment（技术变革与就业的长期争论）", "url": "https://en.wikipedia.org/wiki/Technological_unemployment"},
      ],
    },
    {
      "position": "不要把估值波动等同于技术停滞",
      "holders": "区分「能力曲线」与「资本市场叙事」的研究者与工程师（常见于该帖另一侧的回复）",
      "argument": "公司估值可以在数月内大幅起落，而模型能力、基础设施和配套工具的变化是另一条曲线。即便出现投资寒冬，已训练的方法、开源生态与下游应用仍可能继续扩散。因此「泡沫破裂」描述的是金融现象，不必自动等于「AI 没用了」。",
      "sources": [
        {"title": "Ask HN 原帖讨论", "url": "https://news.ycombinator.com/item?id=50421778"},
      ],
    },
    {
      "position": "宏观生产率与劳动市场的变化可能远慢于炒作",
      "holders": "Daron Acemoglu（2024 年 NBER 工作论文对 AI 宏观效应的估计偏审慎）",
      "argument": "即便部分任务被自动化，总生产率、工资和就业结构的改变仍取决于任务覆盖面、互补性投资与制度。把短期市值当作社会变革已经完成或已经失败的证据，都会过度推断。",
      "sources": [
        {"title": "Acemoglu, The Simple Macroeconomics of AI（NBER w32487）", "url": "https://www.nber.org/papers/w32487"},
      ],
    },
  ],
  "open_parts": "「泡沫」是否成立取决于用哪一套价格与利润标准，事后才能看得更清。AI 对就业与分配的中期影响，以及开源与封闭模型格局会如何演化，都还没有定论。这道题的态度部分也无法由数据单独裁定。",
}

ANSWERS["2026-11-09-biz-robots-jobs"] = {
  "summary": "长期来看，自动化会消灭一些岗位、创造另一些岗位，并改变中间任务的内容。David Autor 等强调：技术既替代也互补劳动，所以「工作会全部消失」的预测多次落空。但具体群体可能因技能与地区而受损。政策讨论因此分裂为：依靠再培训与新行业吸收，或用税收与普遍基本收入等机制重建收入。",
  "views": [
    {
      "position": "自动化会重构工作，但不必然消灭工作本身",
      "holders": "David Autor（2015）；Keynes 早在 1930 年就讨论过技术性失业与闲暇的前景",
      "argument": "历史经验是：节省劳动力的技术会降低某些任务的需求，同时降低价格、提高实际收入并催生新需求。Autor 指出，问题往往不是「完全没有工作」，而是极化——常规中间岗位被压缩，两端任务相对更重要。",
      "sources": [
        {"title": "Autor, Why Are There Still So Many Jobs?（Journal of Economic Perspectives）", "url": "https://www.aeaweb.org/articles?id=10.1257/jep.29.3.3"},
        {"title": "Keynes, Economic Possibilities for our Grandchildren（1930）", "url": "https://www.marxists.org/reference/subject/economics/keynes/1930/our-grandchildren.htm"},
      ],
    },
    {
      "position": "机器人与 AI 可能对局部劳动市场造成实质冲击",
      "holders": "Acemoglu 与 Restrepo；Frey 与 Osborne 对职业可自动化比例的估计常被引用但也有争议",
      "argument": "美国通勤区数据显示，工业机器人暴露度较高的地区，就业与工资受到负面冲击。另有研究按职业任务估计未来可被自动化的比例，数字很大，但「技术上可自动化」不等于「经济上会立即替代」。",
      "sources": [
        {"title": "Acemoglu & Restrepo, Robots and Jobs（NBER w23285）", "url": "https://www.nber.org/papers/w23285"},
        {"title": "Frey & Osborne, The Future of Employment（Oxford Martin）", "url": "https://www.oxfordmartin.ox.ac.uk/publications/the-future-of-employment"},
      ],
    },
    {
      "position": "若工资工作不再覆盖大多数人，需另建收入机制",
      "holders": "普遍基本收入（UBI）的倡导者与政策实验者；词条对其论证与批评有综述",
      "argument": "若大量任务被机器承担，仅靠「再找一份类似的工作」可能不够。UBI、负所得税或工资补贴被提出来保障基本生活并保留选择，但资金来源、劳动供给与政治可行性都有激烈争论。",
      "sources": [
        {"title": "Wikipedia：Universal basic income", "url": "https://en.wikipedia.org/wiki/Universal_basic_income"},
      ],
    },
  ],
  "open_parts": "没有人能可靠预言未来二三十年被替代的净岗位数。再培训是否跟得上、UBI 的财政与激励效应如何、新任务会不会主要流向高技能者，都仍是开放的经验问题。",
}

ANSWERS["2026-11-08-ai-blackbox"] = {
  "summary": "简短的回答是：我们能测量输入输出、可视化部分神经元或特征，但对大型网络「为什么给出这个判断」通常仍缺乏完整、可检验的机制性理解。近年的机械可解释性试图把内部计算分解为特征与回路，并在小模型或有限模块上取得进展，但距离「科学家已经知道网络里在发生什么」还很远。",
  "views": [
    {
      "position": "目前主要是行为层面的成功，机制层面仍是黑箱",
      "holders": "Lipton 对「可解释」宣传的批评；该问题在人工智能 Stack Exchange 上的讨论亦持审慎态度",
      "argument": "高准确率并不等于理解。许多所谓解释是事后拟合的热力图或特征重要性，未必对应网络真正使用的计算。若不能预测模型在分布外或受干预时的行为，就不能说「已经知道内部发生了什么」。",
      "sources": [
        {"title": "Lipton, The Mythos of Model Interpretability (arXiv:1606.03490)", "url": "https://arxiv.org/abs/1606.03490"},
        {"title": "原问题：Do scientists know what is happening inside artificial neural networks?", "url": "https://ai.stackexchange.com/questions/1479/do-scientists-know-what-is-happening-inside-artificial-neural-networks"},
      ],
    },
    {
      "position": "机械可解释性正在把「内部」变成可研究的对象",
      "holders": "Chris Olah 及 Distill / Circuits 传统；Anthropic 的单语义特征等工作",
      "argument": "特征可视化表明某些神经元或方向对应可辨认的概念；进一步的「回路」分析试图追踪特征如何组合。对稀疏自编码器等工具的研究表明，有可能把叠加在一起的特征分解成更可解释的单元，尽管仍不完整。",
      "sources": [
        {"title": "Olah et al., Feature Visualization（Distill, 2017）", "url": "https://distill.pub/2017/feature-visualization/"},
        {"title": "Cammarata et al., Zoom In: An Introduction to Circuits（Distill, 2020）", "url": "https://distill.pub/2020/circuits/zoom-in/"},
        {"title": "Bricken et al., Towards Monosemanticity（Transformer Circuits, 2023）", "url": "https://transformer-circuits.pub/2023/monosemantic-features/index.html"},
      ],
    },
  ],
  "open_parts": "可解释性结果大多来自较小或经过挑选的模型，能否扩展到最强的前沿系统尚不清楚。即便找到可解释的特征，它们是否覆盖模型的主要能力、能否支持可靠的安全保证，仍然没有答案。",
}

ANSWERS["2026-11-08-ai-trolley"] = {
  "summary": "自动驾驶的「该撞谁」把电车难题变成了工程规格问题。实验表明，公众的道德偏好并不一致，而且人们常希望别人的车利人、自己的车利己。许多伦理学与政策讨论因此认为：把罕见的两难当成核心设计问题可能用错了焦点，更应处理风险分配、责任归属与降低事故总量。",
  "views": [
    {
      "position": "必须预先编码社会可接受的碰撞伦理",
      "holders": "Bonnefon、Shariff 与 Rahwan（2016）；后续 Moral Machine 大规模实验",
      "argument": "若算法在不可避免的伤害之间做选择，制造商和监管者无法回避规则。调研显示，人们在抽象层面常支持最小化伤害或保护更多生命，但若规则要求牺牲乘客，购买意愿会下降。这是一个社会困境，而不只是编程题。",
      "sources": [
        {"title": "Bonnefon, Shariff & Rahwan, The social dilemma of autonomous vehicles（PubMed）", "url": "https://pubmed.ncbi.nlm.nih.gov/27339987/"},
        {"title": "Awad et al., The Moral Machine experiment（Nature）", "url": "https://www.nature.com/articles/s41586-018-0637-6"},
        {"title": "Moral Machine 项目网站", "url": "https://www.moralmachine.net/"},
      ],
    },
    {
      "position": "电车框架可能误导真正该监管的问题",
      "holders": "人工智能伦理综述中的审慎立场（如斯坦福哲学百科《Ethics of Artificial Intelligence》所梳理的风险与责任议题）",
      "argument": "真实事故很少呈现教科书式的「只能打方向盘二选一」，更常见的是感知错误、设计权衡和谁来承担责任。过度聚焦虚构两难，可能忽略减速设计、强制标准、保险与刑事责任等更能减少伤害的制度安排。",
      "sources": [
        {"title": "Stanford Encyclopedia of Philosophy：Ethics of Artificial Intelligence", "url": "https://plato.stanford.edu/entries/ethics-ai/"},
        {"title": "Internet Encyclopedia of Philosophy：Ethics of Artificial Intelligence", "url": "https://iep.utm.edu/ethics-of-artificial-intelligence/"},
      ],
    },
  ],
  "open_parts": "不同文化在 Moral Machine 中表现出不同偏好，是否以及如何把它们写入法规，没有共识。责任应落在厂商、软件提供者还是使用者，各国立法仍在演化。如何在保护乘客与减少对外部人的伤害之间取得可执行的平衡，仍未解决。",
}

ANSWERS["2026-11-08-biz-fast-projects"] = {
  "summary": "帝国大厦等案例显示，历史上某些重大工程确实能在极短时间内完工；当代公共工程则常以延期和超支闻名。一种解释是：今天的项目在安全、环保、民主参与和工时制度上更严格，速度换来了其他价值。另一种解释强调激励与管理失败——巨项目系统性过于乐观。也有人指出比较存在生存者偏差：我们记住了过去的成功，却忽略了同时代的失败。",
  "views": [
    {
      "position": "历史上确有极快完工的样本，值得当成对照",
      "holders": "Patrick Collison（问题提出者，并整理了「Fast」案例清单）",
      "argument": "若过去能在数百天内建成摩天楼或战时机场，而今天一条地铁延长线耗时数年，就不能把缓慢当成自然定律。至少应追问：是技术更难了，还是许可、协调和目标函数变了。",
      "sources": [
        {"title": "Patrick Collison, Questions", "url": "https://patrickcollison.com/questions"},
        {"title": "Patrick Collison, Fast（快速完工案例清单）", "url": "https://patrickcollison.com/fast"},
      ],
    },
    {
      "position": "当代巨项目普遍存在乐观偏差与成本低估",
      "holders": "Bent Flyvbjerg",
      "argument": "对全球巨项目的综述表明，超支和延期是常规而非例外，原因包括利益方的策略性低估、参照类预测缺失以及项目独特而难以管理的复杂性。速度下降不一定只是「我们变得更谨慎」，也可能是治理失败。",
      "sources": [
        {"title": "Flyvbjerg, What You Should Know About Megaprojects and Why（arXiv:1409.0003）", "url": "https://arxiv.org/pdf/1409.0003"},
      ],
    },
    {
      "position": "比较基准本身需要非常小心",
      "holders": "José Luis Ricón 对 Collison 问题的长文回应",
      "argument": "把巅峰案例与今天的平均公共项目直接对比，可能不公平：战时动员、不同的劳工与安全标准、以及「被记住的快速项目」都会扭曲印象。要证明「当代系统性变慢」，需要匹配项目类型与约束后再看数据。",
      "sources": [
        {"title": "José Luis Ricón, Building skyscrapers, and spending on major projects（Nintil）", "url": "https://nintil.com/building-skyscrapers-and-spending-on-major-projects"},
      ],
    },
  ],
  "open_parts": "在控制了安全标准与项目复杂度之后，当代公共工程是否「异常缓慢」，还缺少被广泛接受的因果分解。哪些许可改革能提速而不显著增加风险，也缺乏足够的对比实验。",
}

ANSWERS["2026-11-08-sci-science-progress"] = {
  "summary": "对科学进步动力学的一个有影响力的判断是：科研人员和经费大幅增加，但按科学家自己的评价或按全要素生产率来看，重大突破的「单位投入产出」似乎在下降。Bloom、Jones、Van Reenen 与 Webb 用多个领域的数据论证「想法越来越难找」；Collison 与 Nielsen 据此呼吁把科学本身当作需要研究与改进的系统。",
  "views": [
    {
      "position": "想法正变得更难找到，研究生产率在下降",
      "holders": "Nicholas Bloom、Charles Jones、John Van Reenen、Michael Webb",
      "argument": "他们考察半导体、农业、医学和整体经济后发现：维持同样增速所需的研究投入在上升。换言之，不是完全停步，而是必须跑得更用力才能留在原地。这对长期经济增长意味着，仅靠扩大科研规模可能不够。",
      "sources": [
        {"title": "Bloom, Jones, Van Reenen & Webb, Are Ideas Getting Harder to Find?（AER）", "url": "https://www.aeaweb.org/articles?id=10.1257/aer.20180338"},
        {"title": "作者提供的 PDF 版本", "url": "https://www-leland.stanford.edu/~chadj/IdeaPF.pdf"},
      ],
    },
    {
      "position": "需要一门「进步的科学」来改进科学体制本身",
      "holders": "Patrick Collison 与 Michael Nielsen；以及 Collison 与 Tyler Cowen 对进步研究的倡导",
      "argument": "如果效率下降部分来自资助方式、职业激励、发表文化和风险管理，那么改变制度就可能改变曲线。他们主张像研究自然现象一样研究「怎样组织研究更有效」，而不是假定现行大学与资助体系已经最优。",
      "sources": [
        {"title": "Collison & Nielsen, Science Is Getting Less Bang for Its Buck（The Atlantic，Internet Archive 存档）", "url": "https://web.archive.org/web/20201109000000/https://www.theatlantic.com/science/archive/2018/11/diminishing-returns-science/575665/"},
        {"title": "Patrick Collison, Questions", "url": "https://patrickcollison.com/questions"},
      ],
    },
  ],
  "open_parts": "「重要发现」很难客观计量，用论文、专利或专家评选都会有偏差；表面的产出下降也可能来自测量问题或低垂果实已经摘完。制度实验（不同资助模式、团队规模、失败容忍度）的因果证据仍然很少。",
}

ANSWERS["2026-11-08-phil-dreaming"] = {
  "summary": "笛卡尔在《第一哲学沉思》中用梦论证挑战感觉信念：既然梦中的经验可以与清醒时一样生动，我如何保证此刻不是在做梦？一种回应是寻找梦与清醒的内在标记（连贯性、可检验性）；另一种是承认彻底怀疑无法被「从内部」完全驳倒，但认为它不威胁日常知识。此问题在东亚思想中也有庄子梦蝶的表述。",
  "views": [
    {
      "position": "梦论证表明纯感觉经验不足以奠定确定性",
      "holders": "勒内·笛卡尔（沉思录第一、六沉思）",
      "argument": "笛卡尔指出，过去他曾在梦中确信自己坐在炉火旁，因此单凭当下经验的生动性，不能排除自己在做梦。数学等似乎更稳固的真理，他在后文用其他怀疑（如邪恶精灵）继续逼问；就「是不是在做梦」而言，关键是：没有一个仅依赖当前感觉的判决程序。",
      "sources": [
        {"title": "Stanford Encyclopedia of Philosophy：Descartes’ Epistemology", "url": "https://plato.stanford.edu/entries/descartes-epistemology/"},
        {"title": "Stanford Encyclopedia of Philosophy：Dreams and Dreaming", "url": "https://plato.stanford.edu/entries/dreams-dreaming/"},
      ],
    },
    {
      "position": "可用连贯性与可公共检验来区分，尽管不是逻辑保证",
      "holders": "笛卡尔本人在第六沉思提出以记忆连贯等作为标记；当代讨论在 SEP《Dreams and Dreaming》中有综述",
      "argument": "清醒生活的经验可以彼此衔接、接受他人核对和反复实验，而梦往往断裂、难以稳定复验。这类标准在实践中很强，但怀疑论者会说：你也可能只是梦见了「连贯和复验」。因此它更像合理的区分，而不是一劳永逸的证明。",
      "sources": [
        {"title": "SEP：Dreams and Dreaming（含笛卡尔的连贯性标准及批评）", "url": "https://plato.stanford.edu/entries/dreams-dreaming/"},
      ],
    },
  ],
  "open_parts": "彻底的怀疑（「也许一切证据都还在梦中」）无法用再多的经验完全关闭。当代睡眠科学可以描述清醒与 REM 睡眠的差异，但无法从第一人称内部给出逻辑保证。我们究竟需要何种「知道」，仍取决于所采用的知识论标准。",
}

ANSWERS["2026-11-08-phil-edge-believe"] = {
  "summary": "Edge.org 2005 年的年度问题并不是要一个统一答案，而是邀请科学家与思想家公开自己「相信为真却无法证明」的命题。回应大致落在几类：对他人心灵的信念、对尚未证实的宇宙或数学命题的赌注，以及对死后意识是否存在等原则性立场。它揭示的是科学实践也依赖尚未被证明的判断，而不是某条具体定理。",
  "views": [
    {
      "position": "我们无法证明他人有内在体验，但几乎不得不相信",
      "holders": "心理学家 Daniel Gilbert 在 2005 年 Edge 回应中的立场",
      "argument": "Gilbert 写道，即便将来能造出举止完全像人的人工系统，我们也没有判定其是否有主观体验的最终测试；对身边的人，我们同样是在「无法证明」的情况下相信他们有内心生活。他的答案是：我所相信却无法证明的，就是「你」。",
      "sources": [
        {"title": "Edge 2005 回应汇编（含 Gilbert 原文）", "url": "https://www.edge.org/responses/what-do-you-believe-is-true-even-though-you-cannot-prove-it"},
        {"title": "Edge 2005 年度问题页", "url": "https://www.edge.org/annual-question/what-do-you-believe-is-true-even-though-you-cannot-prove-it"},
      ],
    },
    {
      "position": "有些信念原则上可检验，只是今天还没有证据",
      "holders": "BBC 对 Edge 2005 的报道中提到：多位回应者把「地球之外存在生命」当作此类信念；Richard Dawkins 在同一节目中提醒，直觉之后仍应寻求证据",
      "argument": "这类命题与「原则上不可证」不同：它们可能在未来被观测裁决。把它们说成信念，是承认证据不足，而不是主张永远不必论证。",
      "sources": [
        {"title": "Edge 转载的 BBC Radio 4 讨论（含地外生命与 Dawkins 的评论）", "url": "https://www.edge.org/news/fantastically-stimulatingonce-you-start-you-cant-stop-thinking-about-that-question-%E2%80%94-0"},
      ],
    },
    {
      "position": "也有人把「死后意识不复存在」当作无法向自己证明、却划分世界观的判断",
      "holders": "小说家 Ian McEwan 提交给 Edge 的回应（经 BBC 引用）",
      "argument": "McEwan 说，他相信自己的意识不会在死亡后继续存在（除了在他人记忆与文字中淡淡残留），并认为这一划分对思想与社会后果重大。这不是实验室命题，而是对人格与死亡的哲学判断。",
      "sources": [
        {"title": "BBC 节目中引用的 Ian McEwan 回应（Edge 存档）", "url": "https://www.edge.org/news/fantastically-stimulatingonce-you-start-you-cant-stop-thinking-about-that-question-%E2%80%94-0"},
      ],
    },
  ],
  "open_parts": "这道年度问题没有标准答案，也没有一份「应当相信什么」的清单。哪些未证命题属于科学启发式，哪些属于个人形而上学，界线本身就有争议。120 篇回应只能当作样本，不能代表全部科学家。",
}

ANSWERS["2026-11-08-psych-critical"] = {
  "summary": "批判性思维可以被教学改善，但很难当成一种脱离知识、可随意迁移到任何领域的「通用技能」。Daniel Willingham 的影响广泛的综述指出：评估证据、考虑替代解释等思维过程，严重依赖该领域的背景知识；只教抽象策略，往往在新情境中失效。更可行的做法，是在具体学科里反复示范并练习这些策略。",
  "views": [
    {
      "position": "批判性思维很难作为通用技能被直接教会并自动迁移",
      "holders": "Daniel T. Willingham（2007）",
      "argument": "要判断一则论证好不好，必须先知道相关事实与该领域中什么算证据。学生在一种课堂上学会的「批判」步骤，并不会自动迁移到另一门课。因此，把批判性思维理解成可以单独训练的肌肉，会低估知识的作用。",
      "sources": [
        {"title": "Willingham, Critical Thinking: Why Is It So Hard to Teach?（American Educator, 2007）", "url": "https://www.aft.org/ae/summer2007/willingham"},
        {"title": "同一文章的 PDF 版本", "url": "https://www.aft.org/sites/default/files/media/2014/Crit_Thinking.pdf"},
      ],
    },
    {
      "position": "可以教，但必须嵌在学科内容与大量练习里",
      "holders": "Willingham 本人给出的建设性结论；教育心理学中强调「在领域内练习」的传统",
      "argument": "这并不意味着放弃教学。教师可以在历史、科学或数学中明确示范如何权衡证据、如何考虑反例，并提供多次练习。目标应是让学生在特定领域变得更善于思考，而不是指望一次「思维课」改变所有判断。",
      "sources": [
        {"title": "Willingham, 2007（见上，文中同时给出教学建议）", "url": "https://www.aft.org/ae/summer2007/willingham"},
      ],
    },
  ],
  "open_parts": "何种课程能产生可测量、可迁移的长期效果，实验结果并不稳定。标准化测验是否测到了真正的批判性思维，也有争议。动机、认知风格与课堂之外的信息环境，如何调节教学效果，仍待研究。",
}

ANSWERS["2026-11-08-psych-maslow"] = {
  "summary": "马斯洛需求层次是极流行的隐喻，但作为严格科学理论，证据并不支持「必须先完全满足低层、再出现高层」的固定阶梯。跨文化研究显示，基本需要的满足与幸福感相关，可这些需要不必按单一顺序出现。它更适合当作启发性分类，而不是已被证实的心理定律。",
  "views": [
    {
      "position": "需要本身与幸福感有关，但严格层级缺乏支持",
      "holders": "Louis Tay 与 Ed Diener（2011）对全球样本的研究；通识综述见马斯洛层次的百科条目",
      "argument": "Tay 与 Diener 发现，食物、安全、社会关系、尊重与自主等需要的满足，普遍与主观幸福感相关；但人们可以在基本需要未充分满足时仍体验到意义与社会连接。这支持「人类有若干普遍需要」，而不支持「必须逐级解锁」。",
      "sources": [
        {"title": "Tay & Diener, Needs and subjective well-being around the world（PubMed）", "url": "https://pubmed.ncbi.nlm.nih.gov/21688922/"},
        {"title": "Wikipedia：Maslow's hierarchy of needs（含实证研究综述）", "url": "https://en.wikipedia.org/wiki/Maslow%27s_hierarchy_of_needs"},
      ],
    },
    {
      "position": "作为教学隐喻仍有用，但不应当成已证实的阶梯定律",
      "holders": "心理学教材与批评者的常见折中立场（见上述词条对批评史的整理）",
      "argument": "把动机分成若干类型，有助于初学者记住人不全是为了物质刺激而行动。可一旦把它写成不可颠倒的金字塔，并用于管理或教育决策，就越过了证据所能支持的范围。",
      "sources": [
        {"title": "Wikipedia：Maslow's hierarchy of needs", "url": "https://en.wikipedia.org/wiki/Maslow%27s_hierarchy_of_needs"},
      ],
    },
  ],
  "open_parts": "需要应如何分类、是否存在跨文化稳定的结构、自我实现在测量上指什么，都没有统一方案。马斯洛原初文本与后来被简化的「五层金字塔」图也不完全相同，引用时需要区分。",
}

ANSWERS["2026-11-07-ai-paradox"] = {
  "summary": "在科幻里，一句自相矛盾的话就能让计算机起火；在真实的计算理论里，悖论和自指对应的是停机问题、不完备性这类「某些问题不能被一般性地判定」，而不是运行时被「逻辑杀死」。经典逻辑中，从矛盾可以推出任意结论（爆炸原理），因此一个允许任意爆炸的推理引擎会变得无用——但这是设计选择。当代机器学习系统尤其不会因为听到说谎者悖论而停机或损毁。",
  "views": [
    {
      "position": "自指与悖论标出的是不可判定性，不是物理上的「致死」",
      "holders": "图灵关于停机问题的结果；哥德尔不完备定理所划出的形式系统限度",
      "argument": "不存在一个通用算法，能正确判断任意程序是否停机。这限制了「完美自我检查」的能力，也与悖论性自指有关。它说明的是某些问题没有一般算法，而不是给系统输入一句矛盾就会使其崩溃。",
      "sources": [
        {"title": "Wikipedia：Halting problem", "url": "https://en.wikipedia.org/wiki/Halting_problem"},
        {"title": "Stanford Encyclopedia of Philosophy：Gödel’s Incompleteness Theorems", "url": "https://plato.stanford.edu/entries/goedel-incompleteness/"},
        {"title": "Stanford Encyclopedia of Philosophy：Turing Machines", "url": "https://plato.stanford.edu/entries/turing-machine/"},
      ],
    },
    {
      "position": "若系统把爆炸原理用到底，矛盾会让推理变得无用",
      "holders": "经典逻辑中的爆炸原理（ex contradictione quodlibet）",
      "argument": "在标准演绎逻辑里，从 A 且非 A 可以推出任意 B。若一个证明助手或规则引擎在遇到矛盾后仍按此推进，它会「证明」一切，从而丧失鉴别力。工程上通常会隔离矛盾、使用次协调逻辑或拒绝该输入，而不是让机器「死去」。",
      "sources": [
        {"title": "Wikipedia：Principle of explosion", "url": "https://en.wikipedia.org/wiki/Principle_of_explosion"},
      ],
    },
  ],
  "open_parts": "在什么意义上可以把对齐失败或目标冲突称为「被悖论伤害」，更多是比喻。形式系统和统计模型遭遇不一致输入时的安全表现，仍是开放的工程与理论研究问题，但不能从科幻情节直接推论。",
}

ANSWERS["2026-11-07-biz-bloom"] = {
  "summary": "本杰明·布鲁姆 1984 年提出「两标准差问题」：在他所综述的掌握学习与一对一辅导研究中，个别辅导相对常规班级教学可达到约两个标准差的成绩提升。效应是否「普遍为两个标准差」后来常被简化甚至夸大；更稳妥的结论是：高质量的个别化辅导与掌握学习确实能带来可观增益，但如何在不依赖大量人类导师的前提下规模化，仍是开放问题——这也正是布鲁姆原文的出发点。",
  "views": [
    {
      "position": "一对一辅导与掌握学习可以产生很大的学习增益",
      "holders": "Benjamin Bloom（1984）及其所依据的一系列实验",
      "argument": "布鲁姆把「找到与一对一辅导同样有效、又能用于群体教学的方法」称作 2 Sigma Problem。原文的核心观察是：辅导和掌握学习显著优于当时的常规课堂。这意味着学习潜力可能远未被常规教学用尽。",
      "sources": [
        {"title": "Bloom, The 2 Sigma Problem（Educational Researcher, 1984；MIT 转载 PDF）", "url": "https://web.mit.edu/5.95/readings/bloom-two-sigma.pdf"},
        {"title": "Patrick Collison 对该问题的转述与提问", "url": "https://patrickcollison.com/questions"},
      ],
    },
    {
      "position": "关键困难是规模化，而不是再证明「个别化有帮助」",
      "holders": "布鲁姆本人将此表述为待解的教学法问题；后继者讨论智能辅导、掌握学习课程等路径",
      "argument": "若增益主要来自即时反馈、让学生在前进前真正掌握，以及适应个别进度，那么问题就变成：如何用更好的教材、同伴辅导或软件逼近这些条件。是否能在真实学校系统中稳定达到「两个标准差」，不能从早期实验室或小样本研究直接外推。",
      "sources": [
        {"title": "Bloom, The 2 Sigma Problem（见上）", "url": "https://web.mit.edu/5.95/readings/bloom-two-sigma.pdf"},
      ],
    },
  ],
  "open_parts": "原始效应量对今天多样化的课堂、学科和测评是否仍成立，需要新的大规模复制。AI 辅导能否接近人类导师的效果，以及在何种群组中有效，还没有定论。即便有效，公平获取与教师角色如何调整也未解决。",
}

ANSWERS["2026-11-07-biz-wage-gap"] = {
  "summary": "若「完全相同的工作、完全相同的生产率却系统性更低薪」，竞争性企业理应争相雇用被低估的一方以降低成本——这正是该问题的逻辑。经验研究显示，总体性别工资差距中的很大一部分，与职业、行业、工时和职业中断有关；在控制这些因素后仍有残差。残差可以被解释为歧视，也可以被解释为未观测到的差异。两者可以同时存在。",
  "views": [
    {
      "position": "市场竞争会惩罚纯歧视，因此「同工完全不同酬」难以无限持续",
      "holders": "这一逻辑可追溯到 Gary Becker 对歧视的经济学分析；问题本身把该推论问得很尖锐",
      "argument": "若雇主仅仅因为偏见而放弃同样能干、要价更低的劳动者，竞争对手就能用更低成本生产并占领市场。所以，长期持续的差距更可能来自：工作其实并不完全相同、工时与灵活性被不同地奖励，或市场并非充分竞争。",
      "sources": [
        {"title": "Blau & Kahn, The Gender Wage Gap: Extent, Trends, and Explanations（JEL 2017）", "url": "https://www.aeaweb.org/articles?id=10.1257/jel.20160995"},
        {"title": "同一研究的 NBER 工作论文版本（w21913）", "url": "https://www.nber.org/papers/w21913"},
      ],
    },
    {
      "position": "剩余差距很大程度上与工时结构、职业选择和照料负担有关",
      "holders": "Claudia Goldin（2014）；Blau 与 Kahn 的综述",
      "argument": "Goldin 指出，在许多高薪职业中，长时间、连续且不可预测的工作被超级线性地奖励，这会对需要时间灵活性的人（往往更多是承担照料的女性）产生惩罚。缩小差距的关键，可能是改变工作如何被组织与计酬，而不只是「要求雇主只雇更便宜的一方」。",
      "sources": [
        {"title": "Goldin, A Grand Gender Convergence: Its Last Chapter（AER 2014）", "url": "https://www.aeaweb.org/articles?id=10.1257/aer.104.4.1091"},
      ],
    },
    {
      "position": "控制可观测因素后仍可能剩下歧视或摩擦",
      "holders": "Blau 与 Kahn 等强调：歧视、规范与不完全竞争仍可能解释部分残差",
      "argument": "即使竞争会削弱公开的偏见，刻板印象、谈判差异、客户或同事的偏好，以及雇主的市场势力，仍可让差距持续。残差不是歧视的精确度量，也不能被自动当作「已经解释完毕」。",
      "sources": [
        {"title": "Blau & Kahn, 2017（见上）", "url": "https://www.aeaweb.org/articles?id=10.1257/jel.20160995"},
      ],
    },
  ],
  "open_parts": "残差里有多少是歧视、多少是未观测偏好或生产率，无法被单一回归裁定。不同国家和职业的机制也不同。政策应侧重同工同酬执法、育儿支持还是改变超长工时的报酬结构，仍有争论。",
}

ANSWERS["2026-11-07-sci-edge-toolkit"] = {
  "summary": "Edge.org 2011 年的问题邀请人们提出一个应进入大众认知工具箱的科学概念。问题本身借用了 James Flynn 的「简写抽象」（SHA）：像「市场」「安慰剂」「随机样本」这样的概念，能作为一块认知积木被反复使用。回应中反复出现的主题包括：对照实验、双盲，以及其他帮助人抵消直觉偏差的方法。它没有唯一正确答案。",
  "views": [
    {
      "position": "应普及的是「简写抽象」这类可迁移概念",
      "holders": "James Flynn（Edge 在问题陈述中引用其 SHA 概念）",
      "argument": "一个好的科学概念应当可以压缩成短语，却能在许多领域里帮助人提问：样本是否随机？有没有对照？这是不是自然主义谬误？工具箱的价值在于迁移，而不在于记住更多名词。",
      "sources": [
        {"title": "Edge 2011 年度问题页（含 Flynn 的 SHA 说明）", "url": "https://www.edge.org/annual-question/what-scientific-concept-would-improve-everybodys-cognitive-toolkit"},
      ],
    },
    {
      "position": "对照实验是最值得被非科学家使用的工具",
      "holders": "Timo Hannay 在 2011 年的 Edge 回应",
      "argument": "Hannay 认为，面对决策时，本能是内省或开会；科学方法则要求在可能的情况下做对照实验。从日心说到量子力学，许多真相似乎违反常识，正说明实验能把我们从直觉限制中释放出来。商业与政策若更经常设计可比较的试验，可能做出更好的决定。",
      "sources": [
        {"title": "Edge 2011 回应汇编（含 Hannay, The Controlled Experiment）", "url": "https://www.edge.org/responses/what-scientific-concept-would-improve-everybodys-cognitive-toolkit"},
      ],
    },
  ],
  "open_parts": "「哪一个概念最重要」没有客观排序，取决于要纠正的是哪一类错误。知道概念名称，与在有动机、有身份认同的情境中真正使用它，是两回事。如何测量「工具箱改善」，也几乎没有标准。",
}

ANSWERS["2026-11-07-sci-edge-last"] = {
  "summary": "2018 年，John Brockman 把 Edge 年度问题的二十年项目收官为：请你提出「最后一个问题」。这不是在寻找某个将被最终解答的科学难题，而是让回答者交出自己愿意被记住的那一问。已发表的两百多则回应分散在宇宙学、意识、真理、文明风险与人机关系等方向，本身就说明「最后一问」取决于提问者的视野。",
  "views": [
    {
      "position": "最后一问指向宇宙与超智能生命尺度",
      "holders": "物理学家 Max Tegmark",
      "argument": "Tegmark 的问题是：在物理定律允许的限度内，未来的超智能宇宙生命会把哪一个问题当作真正最后的、会一直盘桓的问题？它把「最后」理解成时间与智能的极限，而不是人类此刻的议程。",
      "sources": [
        {"title": "Tegmark 的 Edge 2018 回应", "url": "https://www.edge.org/response-detail/27667"},
        {"title": "Edge 2018 回应汇编", "url": "https://www.edge.org/responses/what-is-the-last-question"},
      ],
    },
    {
      "position": "最后一问指向心灵、真理与人类理解的限度",
      "holders": "英国心理学会综述所引的多位心理学家，如 Jonathan Haidt（「为什么如此难找到真理？」）、Gerd Gigerenzer（「人类直觉能否被还原为算法？」）、Alison Gopnik 等",
      "argument": "相当一部分回应并不问宇宙的终结，而问：大脑如何产生真正的发现、直觉与算法的差别、以及为何求真如此困难。收官之问因此也是一项关于「我们还觉得什么最棘手」的抽样。",
      "sources": [
        {"title": "Ella Rhodes, The last question（The Psychologist / BPS）", "url": "https://www.bps.org.uk/psychologist/last-question"},
        {"title": "Edge 2018 年度问题页", "url": "https://www.edge.org/annual-question/what-is-the-last-question"},
      ],
    },
  ],
  "open_parts": "不存在一个可被全体理性人共同认可的「最后一个问题」。把哪一类问题视为最终问题，取决于价值排序：是宇宙的命运、意识的本质，还是文明能否存续。项目本身已经结束，这些提问仍开放。",
}

ANSWERS["2026-11-07-phil-dangerous"] = {
  "summary": "Edge 2006 年的问题由 Steven Pinker 建议，定义很明确：危险不在于想法被假定为假，而在于它可能为真，并因此冲击道德、政治或自我理解。回应覆盖人性、基因与行为、科学治理、以及「科学正在失控」这类可能自我应验的观念。它同样不是一道有标准答案的题，而是一份关于「哪些真可能令人不安」的思想采样。",
  "views": [
    {
      "position": "「科学正在失控」这一想法本身可能带来危险",
      "holders": "Martin Rees",
      "argument": "Rees 指出，若公众相信科学进步已无法被引导，这种信念可能自我应验：人们会放弃争取更安全、更公平的应用路径。21 世纪的风险更多来自人类行动，需要积极的政策，而不是宿命论。",
      "sources": [
        {"title": "Edge 2006 回应汇编（含 Rees, Science may be 'running out of control'）", "url": "https://www.edge.org/responses/what-is-your-dangerous-idea"},
        {"title": "Edge 2006 年度问题页（注明问题由 Pinker 建议）", "url": "https://www.edge.org/annual-question/2006"},
      ],
    },
    {
      "position": "危险的想法可能是关于人性本身的事实",
      "holders": "David M. Buss（其回应讨论「恶」的演化心理）",
      "argument": "Buss 提出，令人不安之处在于：与其把残暴当作少数疯子的属性，不如认真考虑人类头脑中是否包含曾在演化中起作用、可能导致伤害他人的心理机制。若为真，道德教育与制度设计就不能建立在「正常人天然无害」的假设上。",
      "sources": [
        {"title": "Edge 2006 回应汇编（含 Buss 的条目）", "url": "https://www.edge.org/responses/what-is-your-dangerous-idea"},
        {"title": "Wikipedia 对同名文集的介绍", "url": "https://en.wikipedia.org/wiki/What_Is_Your_Dangerous_Idea%3F"},
      ],
    },
  ],
  "open_parts": "「危险」是相对于特定价值与政治环境而言的，没有中立清单。哪些科学主张真的具有社会风险、公开讨论与限制讨论各有何种代价，本身就是未决的伦理问题。一百多篇回应也不能代表全部知识界。",
}

ANSWERS["2026-11-07-phil-consciousness"] = {
  "summary": "大卫·查尔莫斯所谓「困难问题」问的是：为什么物理过程会伴随主观体验（感受质），而不只是功能与行为。容易的问题包括注意、报告、信息整合等可功能化的机制；困难问题则是体验本身为何存在。物理主义、错觉论与泛心论等给出了截然不同的回应，目前没有实验能单独结案。",
  "views": [
    {
      "position": "存在一个不能被功能解释消化的困难问题",
      "holders": "David Chalmers（1995）；其前驱包括 Thomas Nagel 对「作为一只蝙蝠是什么样」的追问",
      "argument": "即便完整说明了大脑如何分辨刺激、控制行为并口头报告，仍可以想象这些功能在「没有内在感受」的情况下实现。因此，主观体验需要额外的解释，而不是再多一些神经机制图就能自动消失。",
      "sources": [
        {"title": "Chalmers, Facing Up to the Problem of Consciousness（作者 PDF）", "url": "https://www.consc.net/papers/facing.pdf"},
        {"title": "Nagel, What Is It Like to Be a Bat?（JSTOR）", "url": "https://www.jstor.org/stable/2183914"},
        {"title": "Stanford Encyclopedia of Philosophy：Consciousness", "url": "https://plato.stanford.edu/entries/consciousness/"},
      ],
    },
    {
      "position": "所谓困难问题是对直觉的误用，意识就是功能/认知过程",
      "holders": "物理主义与若干「错觉论」或消解策略的主张者（SEP 意识条目有综述）；Daniel Dennett 是广为人知的批评者之一",
      "argument": "一旦注意、报告和分辨都被解释，并不剩下一个额外的「体验实体」需要安置。觉得还缺点什么，可能来自想象的限制或概念混淆。按此路线，困难问题应被消解，而不是被「解决」。",
      "sources": [
        {"title": "SEP：Consciousness（含物理主义与反对意见）", "url": "https://plato.stanford.edu/entries/consciousness/"},
        {"title": "Internet Encyclopedia of Philosophy：Consciousness", "url": "https://iep.utm.edu/consciou/"},
      ],
    },
    {
      "position": "体验是根本的，甚至可能是物质的普遍方面",
      "holders": "泛心论传统；SEP《Panpsychism》条目系统梳理当代复兴",
      "argument": "若从无体验的物理实体中「产生」体验显得不可思议，一种选择是：某种极简的体验属性在基本层面上就存在，复杂意识是其组合。这一路线试图认真对待困难问题，但立刻面对「微观体验如何组合成统一心灵」的组合问题。",
      "sources": [
        {"title": "Stanford Encyclopedia of Philosophy：Panpsychism", "url": "https://plato.stanford.edu/entries/panpsychism/"},
      ],
    },
  ],
  "open_parts": "没有公认的实验可以区分「体验是额外的事实」与「体验可被功能完全捕捉」。整合信息、全局工作空间等科学理论解释的是功能和报告，是否触及感受质仍有争议。AI 是否会有主观体验，目前更多是哲学外推。",
}

ANSWERS["2026-11-07-psych-pseudoscience"] = {
  "summary": "人们接受伪科学，很少只是因为「缺少一张科学知识清单」。哲学与心理学研究强调：人类本就依赖启发式，又会保护身份与既有信念；加上现代信息环境让似是而非的解释更容易传播。科学素养有时甚至会强化极化——人们更会为自己阵营的结论辩护。因此，纠正伪科学既要提高方法意识，也要处理动机与信任。",
  "views": [
    {
      "position": "伪科学利用了普遍的认知策略与划界困难",
      "holders": "科学哲学中关于「科学与伪科学划界」的讨论（SEP 条目综述）",
      "argument": "伪科学常常模仿科学的外表（术语、图表、个案），却回避真正的检验、证伪或可靠的对照。公众若主要靠「看起来像不像科学」来判断，就很容易被这种外表说服。划界标准本身在哲学上就有争议，更增加了识别难度。",
      "sources": [
        {"title": "Stanford Encyclopedia of Philosophy：Science and Pseudo-Science", "url": "https://plato.stanford.edu/entries/pseudo-science/"},
      ],
    },
    {
      "position": "动机与文化认同会塑造「愿意相信什么」",
      "holders": "文化认知研究传统，例如 Kahan 等人关于科学素养与气候风险知觉极化的工作",
      "argument": "当某个主张标志群体身份时，人会更有动力寻找支持自己的理由。Kahan 等发现，在气候变化风险上，科学素养与计算能力更高的人，并不自动更接近科学共识，反而可能更极化。这提示：只「灌输更多科学事实」不一定能减少伪科学认同。",
      "sources": [
        {"title": "Kahan et al., The polarizing impact of science literacy and numeracy on perceived climate change risks", "url": "https://www.nature.com/articles/nclimate1547"},
        {"title": "Wikipedia：Cultural cognition", "url": "https://en.wikipedia.org/wiki/Cultural_cognition"},
      ],
    },
  ],
  "open_parts": "教育、事实核查、身份认同干预各自在何种主题上有效，证据并不整齐。平台推荐算法的作用常被讨论，但因果估计困难。如何在不压制正当异议的前提下减少有害伪科学，仍是开放的规范问题。",
}

ANSWERS["2026-11-07-psych-writing"] = {
  "summary": "「写下来有助于记住」大体成立，但其机制更接近生成、组织与提取练习，而不是纸本身有魔力。Mueller 与 Oppenheimer（2014）曾报告：手写笔记比笔记本记录更有利于概念理解，可能因为手写迫使人转述而非逐字抄录。后续复制并未稳定得到同样优势。更坚实的是测试效应：主动回忆通常优于只是重读或抄写。",
  "views": [
    {
      "position": "手写笔记可能比键盘逐字记录更利于概念理解",
      "holders": "Pam Mueller 与 Daniel Oppenheimer（2014）",
      "argument": "他们的实验发现，用笔记本电脑记笔记的人往往记得多、更近乎逐字，但在概念性问题上表现较差；手写者记得更少，却可能进行了更多加工。作者把原因归于编码深度，而不是「不能多任务」这么简单。",
      "sources": [
        {"title": "Mueller & Oppenheimer, The Pen Is Mightier Than the Keyboard（PubMed）", "url": "https://pubmed.ncbi.nlm.nih.gov/24760141/"},
        {"title": "APS 对该研究的新闻说明", "url": "https://www.psychologicalscience.org/news/releases/take-notes-by-hand-for-better-long-term-comprehension.html"},
      ],
    },
    {
      "position": "手写对打字的优势并不稳定，记忆更取决于如何加工",
      "holders": "Morehead、Dunlosky 与 Rawson（2019）等复制与扩展研究",
      "argument": "复制实验没有一致地复制出手写在概念题或延迟测验上的优势；在某些条件下，记笔记甚至不优于不记笔记。更稳妥的建议是：无论用笔还是键盘，都要避免无思考的逐字抄录，并加入回忆、自测与整理。",
      "sources": [
        {"title": "Morehead, Dunlosky & Rawson, How Much Mightier Is the Pen than the Keyboard…（2019）", "url": "https://link.springer.com/article/10.1007/s10648-019-09468-2"},
        {"title": "The Learning Scientists 对该复制研究的介绍", "url": "https://www.learningscientists.org/blog/2019/2/21-1"},
      ],
    },
    {
      "position": "提取练习（测试效应）是更坚实的记忆原则",
      "holders": "学习科学中的测试效应与生成效应传统",
      "argument": "大量研究表明，尝试把内容从记忆中提取出来，通常比再次阅读更能长期保留。写下要点之所以有用，往往是因为它迫使你生成和提取，而不只是「墨水痕迹」本身。",
      "sources": [
        {"title": "Wikipedia：Testing effect", "url": "https://en.wikipedia.org/wiki/Testing_effect"},
        {"title": "Wikipedia：Generation effect", "url": "https://en.wikipedia.org/wiki/Generation_effect"},
      ],
    },
  ],
  "open_parts": "手写与打字的差异在多大程度上取决于设备、是否可复制粘贴、主题类型和延迟间隔，仍未完全澄清。对屏幕阅读障碍、笔记后期复习方式的研究也还在进行。",
}

ANSWERS["2026-11-07-hn-books"] = {
  "summary": "这道 Ask HN 没有标准书单，而是一份极长的个人见证合集。线程里反复出现的，是改变读者「看待决策、设计与人际」方式的书，而不是某一本被全体同意的经典。常见被点名的包括丹尼尔·卡尼曼的《思考，快与慢》、唐纳德·诺曼的《设计心理学》（The Design of Everyday Things）等；也有人举出传记、文学与专业著作。真正的「答案」是：能改写一个人心智模型的书，高度依赖于他当时缺的是哪一块框架。",
  "views": [
    {
      "position": "改变判断与决策方式的认知科学著作被多次提到",
      "holders": "该帖多位评论者（如用户 erd0s、MediumD 等提到 Thinking, Fast and Slow）",
      "argument": "卡尼曼等人把直觉与偏差变成可讨论的词汇，使读者开始检查自己的判断过程。对许多技术从业者来说，这相当于获得了一套新的自我解释语言，因此常被形容为「改变了看待几乎一切的方式」。",
      "sources": [
        {"title": "Ask HN 原帖：What books changed the way you think about almost everything?", "url": "https://news.ycombinator.com/item?id=19087418"},
      ],
    },
    {
      "position": "改变「看人造物与制度」方式的设计与社会著作同样突出",
      "holders": "评论者 borski、Saturdays 等提到 The Design of Everyday Things；另有人提到 The Power Broker 等",
      "argument": "诺曼的书把「这门为什么这么难用」从自我责备改写成设计失败；这类框架会迁移到门、软件和公共服务。另一些读者则通过城市史或政治传记，改变对权力与制度如何成型的看法。共同点是：书提供了可反复使用的观察镜头。",
      "sources": [
        {"title": "Ask HN 原帖讨论", "url": "https://news.ycombinator.com/item?id=19087418"},
      ],
    },
  ],
  "open_parts": "高票评论不等于对所有人「最有价值」。回忆有选择偏差，书的效应也无法从评论中因果识别。这份线程适合当作地图，不适合当作必读书令。",
}

ANSWERS["2026-11-09-biz-econ-consensus"] = {
  "summary": "经济学家内部常有争论，但在若干议题上其实相当一致，而这些结论往往与常识相反。最经典的是比较优势：即便一方在所有生产上都更强，专业化与贸易仍可让双方获益。芝加哥大学 IGM 专家面板等调查还显示，多数受访经济学家对租金管制改善住房供给、关税增进国民福利持否定态度。公众与专业共识之间的落差，本身就是值得解释的现象。",
  "views": [
    {
      "position": "比较优势等贸易命题是反直觉但广泛接受的核心结果",
      "holders": "自李嘉图以来的标准国际贸易理论；通识表述见比较优势词条",
      "argument": "常识是「只有比别人更强才该出口」。比较优势指出：关键是机会成本。即使一国样样都更高效，专注于相对更优的产品并进口其余，仍可提高总产量。这与「进口就是吃亏」的直觉直接冲突。",
      "sources": [
        {"title": "Wikipedia：Comparative advantage", "url": "https://en.wikipedia.org/wiki/Comparative_advantage"},
        {"title": "Economics Stack Exchange 原问题及讨论", "url": "https://economics.stackexchange.com/questions/20992/what-are-some-results-in-economics-that-are-both-a-consensus-and-far-from-common"},
      ],
    },
    {
      "position": "专家调查显示，租金管制、关税等议题上存在可记录的共识",
      "holders": "芝加哥大学布斯商学院 IGM Economic Experts Panel（租金管制调查有公开存档）",
      "argument": "在 IGM 关于租金管制的调查中，绝大多数受访专家不同意「租金管制在过去数十年显著提升了美国中等收入公民的可负担住房数量和质量」这类说法。类似地，专业意见通常认为，关税作为提高整体国民福利的手段效果很差。这些判断常与政治讨论中的直觉相反。",
      "sources": [
        {"title": "IGM Forum：Rent Control（Internet Archive 存档）", "url": "https://web.archive.org/web/20161211101602/http://www.igmchicago.org/surveys/rent-control"},
      ],
    },
  ],
  "open_parts": "「共识」取决于问哪一群经济学家、如何措辞。对最低工资、产业政策等议题，专业内部分歧更大。即便方向性共识存在，效应大小、分配后果与短期过渡成本，仍需个案估计，不能当成口号直接套用。",
}

ANSWERS["2026-11-08-hn-obscure-ds"] = {
  "summary": "这道 Ask HN 的「解答」是一份社区清单：许多并不冷门于论文、却较少出现在入门课上的结构，反复被提起。概率型结构（布隆过滤器、Skip List、HyperLogLog）、压缩与检索结构（Trie、Rope）、以及分布式中的 CRDT、向量检索中的 HNSW 等，是评论里的高频例子。它们的共同点是：用一点可控制的误差或巧妙布局，换空间或时间上的巨大收益。",
  "views": [
    {
      "position": "概率与近似结构用可控误差换效率",
      "holders": "该帖评论者（如 didip、harporoeder、untererdisch、groby_b 等提到 Bloom Filter、Skip List、HyperLogLog）",
      "argument": "布隆过滤器可以快速判断「一定不在集合中」并允许少量假阳性；跳跃表用随机分层接近平衡树的期望性能；HyperLogLog 能在极小空间里估计基数。当精确集合昂贵时，这类结构非常有用。",
      "sources": [
        {"title": "Ask HN 原帖：What are some cool but obscure data structures you know about?", "url": "https://news.ycombinator.com/item?id=32186203"},
        {"title": "Wikipedia：Bloom filter", "url": "https://en.wikipedia.org/wiki/Bloom_filter"},
        {"title": "Wikipedia：Skip list", "url": "https://en.wikipedia.org/wiki/Skip_list"},
      ],
    },
    {
      "position": "还有一批服务于搜索、并发与特殊遍历的结构",
      "holders": "评论中提到 Trie、Rope、CRDT、并查集、HNSW 等的用户",
      "argument": "前缀树适合共享前缀的字符串压缩与检索；Rope 适合对长文本做高效拼接；CRDT 让副本在无中心协调时也能合并；HNSW 等图结构则用于高维近似近邻搜索。它们在数据库、编辑器和向量检索中广泛存在，只是不一定叫「基础课数据结构」。",
      "sources": [
        {"title": "Ask HN 原帖讨论", "url": "https://news.ycombinator.com/item?id=32186203"},
        {"title": "Malkov & Yashunin, HNSW（arXiv:1603.09320）", "url": "https://arxiv.org/abs/1603.09320"},
      ],
    },
  ],
  "open_parts": "「冷门」取决于社区：在数据库或图形学里常见的结构，对网页开发者可能完全陌生。清单没有完结之日，也很少有单一「最酷」的答案。选择结构仍然要看工作负载与误差容忍度。",
}
