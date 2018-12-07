# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
import json
# Create your models here.
# 一、基本信息
class GeneralInfo(models.Model):
    TITLE = (
        (u'主任医师', u'主任医师'),
        (u'副主任医师', u'副主任医师'),
        (u'主治医师', u'主治医师'),
    )
    BLOOD_TYPE = (
        (u'A', u'A'),
        (u'B', u'B'),
        (u'O', u'O'),
        (u'AB', u'AB'),
    )
    NATION = (
        (u'汉族', u'汉族'),
        (u'蒙族', u'蒙古族'),
        (u'回族', u'回族'),
        (u'藏族', u'藏族'),
        (u'维吾尔族', u'维吾尔族'),
        (u'苗族', u'苗族'),
        (u'彝族', u'彝族'),
        (u'壮族', u'壮族'),
        (u'布依族', u'布依族'),
        (u'朝鲜族', u'朝鲜族'),
        (u'满族', u'满族'),
        (u'侗族', u'侗族'),
        (u'瑶族', u'瑶族'),
        (u'白族', u'白族'),
        (u'土家族', u'土家族'),
        (u'哈尼族', u'哈尼族'),
        (u'哈萨克族', u'哈萨克族'),
        (u'傣族', u'傣族'),
        (u'黎族', u'黎族'),
        (u'傈傈族', u'傈傈族'),
        (u'佤族', u'佤族'),
        (u'畲族', u'畲族'),
        (u'高山族', u'高山族'),
        (u'拉祜族', u'拉祜族'),
        (u'水族', u'水族'),
        (u'东乡族', u'东乡族'),
        (u'纳西族', u'纳西族'),
        (u'景颇族', u'景颇族'),
        (u'科尔克孜族', u'科尔克孜族'),
        (u'土族', u'土族'),
        (u'达斡尔族', u'达斡尔族'),
        (u'仫佬族', u'仫佬族'),
        (u'羌族', u'羌族'),
        (u'布朗族', u'布朗族'),
        (u'撒拉族', u'撒拉族'),
        (u'毛难族', u'毛难族'),
        (u'仡佬族', u'仡佬族'),
        (u'锡伯族', u'锡伯族'),
        (u'阿昌族', u'阿昌族'),
        (u'普米族', u'普米族'),
        (u'塔吉克族', u'塔吉克族'),
        (u'怒族', u'怒族'),
        (u'乌孜别克族', u'乌孜别克族'),
        (u'俄罗斯族', u'俄罗斯族'),
        (u'鄂温克族', u'鄂温克族'),
        (u'崩龙族', u'崩龙族'),
        (u'保安族', u'保安族'),
        (u'裕固族', u'裕固族'),
        (u'京族', u'京族'),
        (u'塔塔尔族', u'塔塔尔族'),
        (u'独龙族', u'独龙族'),
        (u'鄂伦春族', u'鄂伦春族'),
        (u'赫哲族', u'赫哲族'),
        (u'门巴族', u'门巴族'),
        (u'珞巴族', u'珞巴族'),
        (u'基诺族', u'基诺族'),
        (u'其他', u'其他'),
    )
    CAREER = (
        (u'学生', u'学生'),
        (u'个体', u'个体'),
        (u'农民', u'农民'),
        (u'军人', u'军人'),
        (u'工人', u'工人'),
        (u'财会人员', u'财会人员'),
        (u'技术人员', u'技术人员'),
        (u'服务业', u'服务业'),
        (u'科教文卫', u'科教文卫'),
        (u'行政管理', u'行政管理'),
        (u'无业', u'无业'),
        (u'其它', u'其它'),
    )
    ENTRANCE = (
        (u'门诊', u'门诊'),
        (u'病房', u'病房'),
    )
    CULTURE = (
        (u'文盲', u'文盲'),
        (u'小学及以下', u'小学及以下'),
        (u'中学或中专', u'中学或中专'),
        (u'大专', u'大专'),
        (u'本科', u'本科'),
        (u'研究生及以上', u'研究生及以上'),
    )
    MARRIAGE = (
        (u'未婚无性生活', u'未婚无性生活'),
        (u'未婚有性生活', u'未婚有性生活'),
        (u'已婚同居', u'已婚同居'),
        (u'已婚分居', u'已婚分居'),
        (u'离婚', u'离婚'),
    )
    owner = models.ForeignKey('myusers.MyUser', related_name='mygi',
                              on_delete=models.CASCADE)  # related name used in serializer for relation

    recdate = models.DateField(verbose_name=u'日期', blank=True, default=date.today, help_text="日期")
    serial = models.CharField(verbose_name=u'问卷编码', max_length=50, help_text="问卷编码")
    hospital = models.CharField(verbose_name=u'医院名称', max_length=100, help_text="医院名称")
    expert = models.CharField(verbose_name=u'填表专家姓名', max_length=50, help_text="填表专家姓名")
    title = models.CharField(verbose_name=u'职称', choices=TITLE, max_length=30, help_text="职称")
    name = models.CharField(verbose_name=u'患者姓名', max_length=50, help_text="患者姓名")
    telephone = models.CharField(verbose_name=u'电话', max_length=20, help_text="电话")
    age = models.IntegerField(verbose_name=u'年龄', help_text="年龄")
    height = models.IntegerField(verbose_name=u'身高cm', help_text="身高cm")
    weight = models.DecimalField(verbose_name=u'体重kg', max_digits=4, decimal_places=1, help_text="体重kg")
    blood_type = models.CharField(verbose_name=u'血型', choices=BLOOD_TYPE, max_length=10, help_text="血型")
    nation = models.CharField(verbose_name=u'民族', choices=NATION, max_length=20, help_text="民族(汉字)")
    career = models.CharField(verbose_name=u'职业', choices=CAREER, max_length=20, help_text="职业")

    # 一般情况-特殊工作环境
    # spec_env = models.ForeignKey(GeneralSpecEnv, on_delete=models.CASCADE)
    gaokong = models.BooleanField(verbose_name=u'高空', default=False, help_text="高空")
    diwen = models.BooleanField(verbose_name=u'低温', default=False, help_text="低温")
    zaosheng = models.BooleanField(verbose_name=u'噪声', default=False, help_text="噪声")
    fushe = models.BooleanField(verbose_name=u'辐射', default=False, help_text="辐射")
    huagongyinran = models.BooleanField(verbose_name=u'化工印染', default=False, help_text="化工印染")
    julieyundong = models.BooleanField(verbose_name=u'剧烈运动', default=False, help_text="剧烈运动")
    qiyou = models.BooleanField(verbose_name=u'汽油', default=False, help_text="汽油")
    wu = models.BooleanField(verbose_name=u'无', default=False, help_text="无")

    address = models.CharField(verbose_name=u'病人现住址', max_length=100, help_text="病人住址")
    entrance = models.CharField(verbose_name=u'病人来源', choices=ENTRANCE, max_length=10, help_text="病人来源")
    culture = models.CharField(verbose_name=u'文化程度', choices=CULTURE, max_length=30, help_text="文化程度")
    marriage = models.CharField(verbose_name=u'婚姻状况', choices=MARRIAGE, max_length=30, help_text="婚姻状况")

    # 一般情况-饮食偏好
    # eat_hobbies = models.ForeignKey(GeneralEatHobbies, on_delete=models.CASCADE)
    wuteshu = models.BooleanField(verbose_name=u'无特殊', default=False, help_text="无特殊")
    sushi = models.BooleanField(verbose_name=u'素食', default=False, help_text="素食")
    suan = models.BooleanField(verbose_name=u'酸', default=False, help_text="酸")
    tian = models.BooleanField(verbose_name=u'甜', default=False, help_text="甜")
    xian = models.BooleanField(verbose_name=u'咸', default=False, help_text="咸")
    xinla = models.BooleanField(verbose_name=u'辛辣', default=False, help_text="辛辣")
    you = models.BooleanField(verbose_name=u'油', default=False, help_text="油")
    shengleng = models.BooleanField(verbose_name=u'生冷', default=False, help_text="生冷")
    kafei = models.BooleanField(verbose_name=u'含咖啡因食物或饮品', default=False, help_text="咖啡因")
    qita = models.CharField(verbose_name=u'其它', max_length=50, default=u'无', help_text="其他")

    def __int__(self):
        return self.name

    def __str__(self):
        return '%d, %s, %s' % (self.id, self.serial, self.name)

    class Meta:
        verbose_name = u'基本信息'
        ordering = ('recdate',)
        permissions = (
            ("prj001_operation", "prj001_all_permissions"),
        )

        verbose_name_plural = verbose_name


################################################################################
# 二、月经情况
class Menstruation(models.Model):
    ABNORMAL = (
        (u'或提前7天以上', u'或提前7天以上'),
        (u'或1月多次', u'或1月多次'),
        (u'或数月1次', u'或数月1次'),
    )
    CYCLICITY_SUM = (
        (u'不足2天', u'不足2天'),
        (u'3-7天', u'3-7天'),
        (u'7天以上', u'7天以上'),
        (u'有时几日即净，有时7日以上甚至达半月余不净', u'有时几日即净，有时7日以上甚至达半月余不净'),
    )
    BLOOD_COND = (
        (u'出血量中等，每次约需5-20张卫生巾', u'出血量中等，每次约需5-20张卫生巾'),
        (u'出血量多，每次多于20张卫生巾', u'出血量多，每次多于20张卫生巾'),
        (u'经量少，每次少于5张卫生巾', u'经量少，每次少于5张卫生巾'),
        (u'经量极少，几乎不用卫生巾，用护垫即可', u'经量极少，几乎不用卫生巾，用护垫即可'),
    )
    BLOOD_COLOR = (
        (u'淡红', u'淡红'),
        (u'鲜红', u'鲜红'),
        (u'暗红', u'暗红'),
        (u'紫红', u'紫红'),
        (u'紫黯', u'紫黯'),
        (u'紫黑', u'紫黑'),
        (u'褐色', u'褐色'),
        (u'其他', u'其他'),
    )
    BLOOD_QUALITY = (
        (u'正常', u'正常'),
        (u'粘稠', u'粘稠'),
        (u'清稀', u'清稀'),
    )
    BLOOD_BLOCK = (
        (u'无', u'无'),
        (u'偶有', u'偶有'),
        (u'常夹少量小血块', u'常夹少量小血块'),
        (u'常夹较大血块', u'常夹较大血块'),
    )
    BLOOD_CHARACTER = (
        (u'顺畅', u'顺畅'),
        (u'势急暴下', u'势急暴下'),
        (u'淋漓不断', u'淋漓不断'),
        (u'点滴即净', u'点滴即净'),
    )

    person = models.OneToOneField(GeneralInfo, related_name='menstruation', on_delete=models.CASCADE)
    owner = models.ForeignKey('myusers.MyUser', related_name='mymenstruation', on_delete=models.CASCADE)

    first_time = models.IntegerField(verbose_name=u'初潮年龄', help_text="初潮年龄")
    cyclicity = models.BooleanField(verbose_name=u'月经周期是否规律', default=False, help_text="月经周期是否规律")
    normal = models.IntegerField(verbose_name=u'月经周期尚规律的间隔天数', blank=True, null=True, help_text="月经周期尚规律的间隔天数")
    abnormal = models.CharField(verbose_name=u'月经不规律的情况', choices=ABNORMAL, max_length=30, blank=True,
                                null=True, help_text="月经不规律的情况")
    cyclicity_sum = models.CharField(verbose_name=u'行经天数', choices=CYCLICITY_SUM, max_length=100, help_text="行经天数")
    blood_cond = models.CharField(verbose_name=u'出血所需卫生巾数', choices=BLOOD_COND, max_length=100, help_text="出血所需卫生巾数")
    blood_color = models.CharField(verbose_name=u'出血颜色', choices=BLOOD_COLOR, max_length=10, help_text="出血颜色")
    blood_quality = models.CharField(verbose_name=u'出血质地', choices=BLOOD_QUALITY, max_length=10, help_text="出血质地")
    blood_block = models.CharField(verbose_name=u'血块', choices=BLOOD_BLOCK, max_length=30, help_text="血块")
    blood_character = models.CharField(verbose_name=u'出血特点', choices=BLOOD_CHARACTER, max_length=20, help_text="出血特点")

    class Meta:
        verbose_name = u'月经情况'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%d" % self.id


################################################################################
# 三、全身症状
class Symptom(models.Model):
    person = models.OneToOneField(GeneralInfo, related_name='symptom', on_delete=models.CASCADE)
    owner = models.ForeignKey('myusers.MyUser', related_name='mysymptom', on_delete=models.CASCADE)

    # 全身症状-精神
    # spirit = models.ForeignKey(SymptomSpirit, on_delete=models.CASCADE)
    spirit_jinglichongpei = models.BooleanField(verbose_name=u'精力充沛', default=False, help_text="精力充沛")
    spirit_jianwang = models.BooleanField(verbose_name=u'健忘', default=False, help_text="健忘")
    spirit_jingshenbujizhong = models.BooleanField(verbose_name=u'精神不集中', default=False, help_text="精神不集中")
    spirit_shenpifali = models.BooleanField(verbose_name=u'神疲乏力', default=False, help_text="神疲乏力")
    spirit_yalida = models.BooleanField(verbose_name=u'学习、工作压力大', default=False, help_text="学习压力大")
    spirit_jiaodabiangu = models.BooleanField(verbose_name=u'个人/家庭遭遇较大变故', default=False, help_text="个人/家庭遭遇较大变故")
    spirit_beishangyuku = models.BooleanField(verbose_name=u'悲伤欲哭', default=False, help_text="悲伤欲哭")

    # 全身症状-情绪
    # mood = models.ForeignKey(SymptomMood, on_delete=models.CASCADE)
    mood_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    mood_leguankailang = models.BooleanField(verbose_name=u'乐观开朗', default=False, help_text="乐观开朗")
    mood_silvguodu = models.BooleanField(verbose_name=u'思虑过度', default=False, help_text="思虑过度")
    mood_xinuwuchang = models.BooleanField(verbose_name=u'喜怒无常', default=False, help_text="喜怒无常")
    mood_fanzaoyinu = models.BooleanField(verbose_name=u'烦躁易怒', default=False, help_text="烦躁易怒")
    mood_jiaolv = models.BooleanField(verbose_name=u'焦虑', default=False, help_text="焦虑")
    mood_beishangyuku = models.BooleanField(verbose_name=u'悲伤欲哭', default=False, help_text="悲伤欲哭")
    mood_yiyu = models.BooleanField(verbose_name=u'抑郁', default=False, help_text="抑郁")
    mood_duosiduolv = models.BooleanField(verbose_name=u'多思多虑', default=False, help_text="多思多虑")
    mood_qita = models.CharField(verbose_name=u'其它', max_length=50, default=u'无', help_text="其他")

    # 全身症状-寒热
    # chill_fever = models.ForeignKey(SymptomChillFever, on_delete=models.CASCADE)
    chillfever_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    chillfever_weihan = models.BooleanField(verbose_name=u'畏寒', default=False, help_text="畏寒")
    chillfever_wuxinfanre = models.BooleanField(verbose_name=u'五心烦热', default=False, help_text="无心烦躁")
    chillfever_wuhouchaore = models.BooleanField(verbose_name=u'午后潮热', default=False, help_text="午后潮热")
    chillfever_direbutui = models.BooleanField(verbose_name=u'低热不退', default=False, help_text="低热不退")

#--------------------------
    # 全身症状-出汗
    sweat_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    sweat_duohan = models.BooleanField(verbose_name=u'多汗', default=False, help_text="多汗")
    sweat_mingxian = models.BooleanField(verbose_name=u'稍微活动则汗出明显', default=False, help_text="稍微活动则汗明显")
    sweat_zihan = models.BooleanField(verbose_name=u'自汗', default=False, help_text="自汗")
    sweat_daohan = models.BooleanField(verbose_name=u'盗汗', default=False, help_text="盗汗")
    sweat_hongre = models.BooleanField(verbose_name=u'烘热汗出', default=False, help_text="烘热汗出")
    sweat_chaore = models.BooleanField(verbose_name=u'潮热汗出', default=False, help_text="潮热汗出")

    #全身症状-语音
    sound_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    sound_qiduan = models.BooleanField(verbose_name=u'气短', default=False, help_text="气短")
    sound_xitanxi = models.BooleanField(verbose_name=u'喜叹息', default=False, help_text="西叹息")
    sound_shaoqilanyan = models.BooleanField(verbose_name=u'少气懒言', default=False, help_text="少气懒言")

    #全身症状-面色
    face_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    face_danbaiwuhua = models.BooleanField(verbose_name=u'淡白无华', default=False, help_text="淡白无华")
    face_cangbai = models.BooleanField(verbose_name=u'苍白', default=False, help_text="苍白")
    face_qingbai = models.BooleanField(verbose_name=u'清白', default=False, help_text="清白")
    face_weihuang = models.BooleanField(verbose_name=u'萎黄', default=False, help_text="微黄")
    face_huangzhong = models.BooleanField(verbose_name=u'黄肿', default=False, help_text="黄肿")
    face_chaohong = models.BooleanField(verbose_name=u'潮红', default=False, help_text="潮红")
    face_huian = models.BooleanField(verbose_name=u'晦暗', default=False, help_text="晦暗")
    face_baierfuzhong = models.BooleanField(verbose_name=u'白而浮肿', default=False, help_text="白而浮肿")
    face_baierandan = models.BooleanField(verbose_name=u'白而黯淡', default=False, help_text="白而黯淡")
    face_mianmulihei = models.BooleanField(verbose_name=u'面目黧黑', default=False, help_text="面目黧黑")
    face_shaohua = models.BooleanField(verbose_name=u'少华', default=False, help_text="少华")
    face_wuhua = models.BooleanField(verbose_name=u'无华', default=False, help_text="无华")

    # 全身症状-心
    heart_zhengcheng = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    heart_xinfan = models.BooleanField(verbose_name=u'心烦', default=False, help_text="心烦")
    heart_xinji = models.BooleanField(verbose_name=u'心悸', default=False, help_text="心悸")

    # 全身症状-乳房
    breast_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    breast_biezhang = models.BooleanField(verbose_name=u'憋胀', default=False, help_text="憋涨")
    breast_citong = models.BooleanField(verbose_name=u'刺痛', default=False, help_text="刺痛")
    breast_zhangtong = models.BooleanField(verbose_name=u'胀痛', default=False, help_text="胀痛")
    breast_chutong = models.BooleanField(verbose_name=u'触痛', default=False, help_text="触痛")

    # 全身症状-胸胁
    chest_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    chest_zhangmen = models.BooleanField(verbose_name=u'胀闷', default=False, help_text="涨闷")
    chest_yintong = models.BooleanField(verbose_name=u'隐痛', default=False, help_text="隐痛")
    chest_citong = models.BooleanField(verbose_name=u'刺痛', default=False, help_text="刺痛")

    # 全身症状-腰膝
    waist_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    waist_suantong = models.BooleanField(verbose_name=u'酸痛', default=False, help_text="酸痛")
    waist_suanruan = models.BooleanField(verbose_name=u'酸软', default=False, help_text="酸软")
    waist_suanleng = models.BooleanField(verbose_name=u'酸冷', default=False, help_text="酸冷")
    waist_lengtong = models.BooleanField(verbose_name=u'冷痛', default=False, help_text="冷痛")
    waist_yaotongrushe = models.BooleanField(verbose_name=u'腰痛如折', default=False, help_text="腰痛如折")

    # 全身症状-腹部
    stomach_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    stomach_zhangtongjuan = models.BooleanField(verbose_name=u'胀痛拒按', default=False, help_text="胀痛据按")
    stomach_xiaofuzhuizhang = models.BooleanField(verbose_name=u'小腹坠胀', default=False, help_text="小腹坠胀")
    stomach_xiaofubiezhang = models.BooleanField(verbose_name=u'小腹憋胀', default=False, help_text="小腹憋胀")
    stomach_xiaofulengtong = models.BooleanField(verbose_name=u'小腹冷痛', default=False, help_text="小腹冷痛")
    stomach_xiaofuzhuotong = models.BooleanField(verbose_name=u'小腹灼痛', default=False, help_text="小腹灼痛")
    stomach_yintongxian = models.BooleanField(verbose_name=u'隐痛喜按', default=False, help_text="隐痛喜按")
    stomach_dewentongjian = models.BooleanField(verbose_name=u'冷痛，得温痛减', default=False, help_text="冷痛,得温痛减")
    stomach_tongruzhenci = models.BooleanField(verbose_name=u'小腹结块，痛如针刺', default=False, help_text="小腹结块,痛如针刺")
    stomach_kongzhui = models.BooleanField(verbose_name=u'有空坠感', default=False, help_text="有空缀感")
    #---------------------------

    # 全身症状-头
    head_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    head_touyun = models.BooleanField(verbose_name=u'头晕', default=False, help_text="头晕")
    head_toutong = models.BooleanField(verbose_name=u'头痛', default=False, help_text="头痛")
    head_touchenzhong = models.BooleanField(verbose_name=u'头沉重', default=False, help_text="头沉重")

    # 全身症状-目
    eyes_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    eyes_muxuan = models.BooleanField(verbose_name=u'目眩', default=False, help_text="目眩")
    eyes_muse = models.BooleanField(verbose_name=u'目涩', default=False, help_text="目涩")
    eyes_yanhua = models.BooleanField(verbose_name=u'眼花', default=False, help_text="眼花")
    eyes_mutong = models.BooleanField(verbose_name=u'目痛', default=False, help_text="目痛")
    eyes_muyang = models.BooleanField(verbose_name=u'目痒', default=False, help_text="目痒")
    eyes_chenqifz = models.BooleanField(verbose_name=u'晨起眼睑浮肿', default=False, help_text="晨起眼浮肿")

    # 全身症状-耳
    ear_erming = models.BooleanField(verbose_name=u'耳鸣', default=False, help_text="耳鸣")
    ear_erlong = models.BooleanField(verbose_name=u'耳聋', default=False, help_text="耳聋")
    ear_tinglibq = models.BooleanField(verbose_name=u'听力不清，声音重复', default=False, help_text="听力不清,声音重复")

    # 全身症状-咽喉
    throat_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    throat_yangan = models.BooleanField(verbose_name=u'咽干', default=False, help_text="咽干")
    throat_yantong = models.BooleanField(verbose_name=u'咽痛', default=False, help_text="咽痛")
    throat_yanyang = models.BooleanField(verbose_name=u'咽痒', default=False, help_text="烟痒")
    throat_yiwugan = models.BooleanField(verbose_name=u'异物感', default=False, help_text="异物感")

    # 全身症状-口味
    breath_wuyiwei = models.BooleanField(verbose_name=u'口中无异味', default=False, help_text="口中无异味")
    breath_kouku = models.BooleanField(verbose_name=u'口苦', default=False, help_text="口苦")
    breath_kougan = models.BooleanField(verbose_name=u'口干', default=False, help_text="口干")
    breath_koudan = models.BooleanField(verbose_name=u'口淡', default=False, help_text="口淡")
    breath_kouxian = models.BooleanField(verbose_name=u'口咸', default=False, help_text="口咸")
    breath_koutian = models.BooleanField(verbose_name=u'口甜', default=False, help_text="口甜")
    breath_kounian = models.BooleanField(verbose_name=u'口粘', default=False, help_text="口粘")
    breath_danyuss = models.BooleanField(verbose_name=u'但欲漱水不欲咽', default=False, help_text="但欲漱口不遇咽")

    # 全身症状-饮食
    diet_nadaishishao = models.BooleanField(verbose_name=u'纳呆食少', default=False, help_text="纳呆食少")
    diet_shiyuws = models.BooleanField(verbose_name=u'食欲旺盛，多食易饥', default=False, help_text="食欲旺盛,多食易饿")
    diet_yanshi = models.BooleanField(verbose_name=u'厌食', default=False, help_text="厌食")
    diet_xireyin = models.BooleanField(verbose_name=u'喜热饮', default=False, help_text="喜热饮")
    diet_xilengyin = models.BooleanField(verbose_name=u'喜冷饮', default=False, help_text="喜冷饮")
    diet_shiyujiantui = models.BooleanField(verbose_name=u'食欲减退，食少', default=False, help_text="食欲减退,食少")
    diet_shihoufuzhang = models.BooleanField(verbose_name=u'食后腹胀', default=False, help_text="食后腹胀")
    diet_shixinla = models.BooleanField(verbose_name=u'喜辛辣', default=False, help_text="喜辛辣")
    diet_shishengleng = models.BooleanField(verbose_name=u'喜生冷', default=False, help_text="喜生冷")
    diet_kebuduoyin = models.BooleanField(verbose_name=u'渴不多饮', default=False, help_text="渴不多饮")

    # 全身症状-睡眠
    sleep_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    sleep_yiban = models.BooleanField(verbose_name=u'一般', default=False, help_text="一般")
    sleep_duomengyixing = models.BooleanField(verbose_name=u'多梦易醒', default=False, help_text="多梦易醒")
    sleep_nanyirumian = models.BooleanField(verbose_name=u'难以入眠', default=False, help_text="难以入眠")
    sleep_cheyebumian = models.BooleanField(verbose_name=u'彻夜不眠', default=False, help_text="彻夜不眠")
    sleep_duomeng = models.BooleanField(verbose_name=u'多梦', default=False, help_text="多梦")
    sleep_shishui = models.BooleanField(verbose_name=u'嗜睡', default=False, help_text="嗜睡")

    # 全身症状-大便
    stool_sehuang = models.BooleanField(verbose_name=u'色黄，通畅，成形不干燥', default=False, help_text="色黄,通畅,成型不干燥")
    stool_bianmi = models.BooleanField(verbose_name=u'便秘', default=False, help_text="便秘")
    stool_zhixi = models.BooleanField(verbose_name=u'质稀', default=False, help_text="质稀")
    stool_sgsx = models.BooleanField(verbose_name=u'时干时稀', default=False, help_text="时干时稀")
    stool_xiexie = models.BooleanField(verbose_name=u'泄泻', default=False, help_text="泄泻")
    stool_tlzqxiexie = models.BooleanField(verbose_name=u'天亮前泄泻', default=False, help_text="天亮前泄泻")
    stool_zhinian = models.BooleanField(verbose_name=u'质黏，有排不尽之感', default=False, help_text="质粘,有排不进之感")
    stool_weixiaohua = models.BooleanField(verbose_name=u'大便中夹有未消化食物', default=False, help_text="大便中夹有未消化实物")

    # 全身症状-小便
    urine_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    urine_duanchi = models.BooleanField(verbose_name=u'短赤', default=False, help_text="短赤")
    urine_duanhuang = models.BooleanField(verbose_name=u'短黄', default=False, help_text="短黄")
    urine_qingchang = models.BooleanField(verbose_name=u'清长', default=False, help_text="清长")
    urine_yeniaopin = models.BooleanField(verbose_name=u'夜尿频', default=False, help_text="夜尿频")
    urine_xbpinshu = models.BooleanField(verbose_name=u'小便频数', default=False, help_text="小便频数")
    urine_niaoji = models.BooleanField(verbose_name=u'尿急', default=False, help_text="尿急")
    urine_niaotong = models.BooleanField(verbose_name=u'尿痛', default=False, help_text="尿痛")
    urine_shaoniao = models.BooleanField(verbose_name=u'少尿', default=False, help_text="少尿")
    urine_yulibujin = models.BooleanField(verbose_name=u'余沥不尽', default=False, help_text="余力不尽")

    # 全身症状-四肢
    limb_zhengchang = models.BooleanField(verbose_name=u'正常', default=False, help_text="正常")
    limb_wuli = models.BooleanField(verbose_name=u'无力', default=False, help_text="无力")
    limb_mamu = models.BooleanField(verbose_name=u'麻木', default=False, help_text="麻木")
    limb_kunzhong = models.BooleanField(verbose_name=u'困重', default=False, help_text="困重")
    limb_zhileng = models.BooleanField(verbose_name=u'肢冷', default=False, help_text="四肢冷")
    limb_bingliang = models.BooleanField(verbose_name=u'冰凉', default=False, help_text="冰凉")
    limb_szxinre = models.BooleanField(verbose_name=u'手足心热', default=False, help_text="手足心热")
    limb_fuzhong = models.BooleanField(verbose_name=u'浮肿', default=False, help_text="浮肿")

    # 全身症状-其他
    other_wu = models.BooleanField(verbose_name=u'无', default=False, help_text="无")
    other_czjdanbai = models.BooleanField(verbose_name=u'唇爪甲淡白', default=False, help_text="唇爪甲淡白")
    other_xyjiantui = models.BooleanField(verbose_name=u'性欲减退', default=False, help_text="性欲减退")

    # 全身症状-舌质
    texture_danhong = models.BooleanField(verbose_name=u'淡红', default=False, help_text="淡红")
    texture_danbai = models.BooleanField(verbose_name=u'淡白', default=False, help_text="淡白")
    texture_pianhong = models.BooleanField(verbose_name=u'偏红', default=False, help_text="偏红")
    texture_danan = models.BooleanField(verbose_name=u'淡黯', default=False, help_text="淡黯")
    texture_zian = models.BooleanField(verbose_name=u'紫黯', default=False, help_text="紫黯")
    texture_yudian = models.BooleanField(verbose_name=u'有瘀点或瘀斑', default=False, help_text="有淤点或淤斑")

    # 全身症状-舌苔
    coating_bai = models.BooleanField(verbose_name=u'白', default=False, help_text="白")
    coating_huang = models.BooleanField(verbose_name=u'黄', default=False, help_text="黄")
    coating_ni = models.BooleanField(verbose_name=u'腻', default=False, help_text="腻")
    coating_bo = models.BooleanField(verbose_name=u'薄', default=False, help_text="薄")
    coating_hou = models.BooleanField(verbose_name=u'厚', default=False, help_text="厚")
    coating_run = models.BooleanField(verbose_name=u'润', default=False, help_text="润")
    coating_hua = models.BooleanField(verbose_name=u'滑', default=False, help_text="滑")
    coating_hhouni = models.BooleanField(verbose_name=u'黄厚腻', default=False, help_text="黄厚腻")
    coating_bairun = models.BooleanField(verbose_name=u'白润', default=False, help_text="白润")
    coating_huangcao = models.BooleanField(verbose_name=u'黄糙', default=False, help_text="黄糙")
    coating_wutai = models.BooleanField(verbose_name=u'无苔', default=False, help_text="无苔")
    coating_shaotai = models.BooleanField(verbose_name=u'少苔', default=False, help_text="少苔")
    coating_huabo = models.BooleanField(verbose_name=u'花剥', default=False, help_text="花剥")

    # 全身症状-舌体
    tongue_shoubo = models.BooleanField(verbose_name=u'瘦薄', default=False, help_text="瘦薄")
    tongue_pangda = models.BooleanField(verbose_name=u'胖大', default=False, help_text="胖大")
    tongue_bianjianhong = models.BooleanField(verbose_name=u'边尖红', default=False, help_text="边尖红")
    tongue_youchihen = models.BooleanField(verbose_name=u'有齿痕', default=False, help_text="有齿痕")
    tongue_zhongyouliewen = models.BooleanField(verbose_name=u'中有裂纹', default=False, help_text="中有裂纹")

    # 全身症状-脉象
    pulse_shi = models.BooleanField(verbose_name=u'实', default=False, help_text="实")
    pulse_fu = models.BooleanField(verbose_name=u'浮', default=False, help_text="浮")
    pulse_chen = models.BooleanField(verbose_name=u'沉', default=False, help_text="沉")
    pulse_chi = models.BooleanField(verbose_name=u'迟', default=False, help_text="迟")
    pulse_huan = models.BooleanField(verbose_name=u'缓', default=False, help_text="缓")
    pulse_xi = models.BooleanField(verbose_name=u'细', default=False, help_text="细")
    pulse_ruo = models.BooleanField(verbose_name=u'弱', default=False, help_text="弱")
    pulse_shu = models.BooleanField(verbose_name=u'数', default=False, help_text="数")
    pulse_hua = models.BooleanField(verbose_name=u'滑', default=False, help_text="滑")
    pulse_se = models.BooleanField(verbose_name=u'涩', default=False, help_text="涩")
    pulse_xian = models.BooleanField(verbose_name=u'弦', default=False, help_text="炫")
    pulse_jin = models.BooleanField(verbose_name=u'紧', default=False, help_text="紧")
    pulse_kou = models.BooleanField(verbose_name=u'芤', default=False, help_text="芤")
    pulse_ru = models.BooleanField(verbose_name=u'濡', default=False, help_text="濡")
    pulse_hong = models.BooleanField(verbose_name=u'洪', default=False, help_text="洪")
    pulse_youli = models.BooleanField(verbose_name=u'有力', default=False, help_text="有力")
    pulse_wuli = models.BooleanField(verbose_name=u'无力', default=False, help_text="无力")

    class Meta:
        verbose_name = u'全身症状'

        verbose_name_plural = verbose_name


################################################################################
# 四、其它
class Other(models.Model):
    BORNCOND = (
        (u'早产（28周-37周）', u'早产（28周-37周）'),
        (u'足月产', u'足月产'),
        (u'阴道分娩', u'阴道分娩'),
        (u'剖宫产', u'剖宫产'),
    )
    BODYCOND = (
        (u'好', u'好'),
        (u'一般', u'一般'),
        (u'易疲劳乏力', u'易疲劳乏力'),
    )
    CAREERLABOR = (
        (u'重体力劳动（如：搬运工、清洁工、农场工人、畜牧场工人等）', u'重体力劳动（如：搬运工、清洁工、农场工人、畜牧场工人等）'),
        (u'中体力劳动（如：家政服务人员、服务生、厨师、护士等）', u'中体力劳动（如：家政服务人员、服务生、厨师、护士等）'),
        (u'轻体力劳动（如：教师、美容美发师、批发商、职员等）', u'中体力劳动（如：教师、美容美发师、批发商、职员等）'),
        (u'坐式的工作（如：收银员、出纳员、接线员、秘书等）', u'坐式的工作（如：收银员、出纳员、接线员、秘书等）'),
    )
    POORBLOOD = (
        (u'不详', u'不详'),
        (u'贫血', u'贫血'),
        (u'不贫血', u'不贫血'),
    )
    PHYCIALEXER = (
        (u'无', u'无'),
        (u'很少（≤1次/周）', u'很少（≤1次/周）'),
        (u'偶尔（≤3次/周）', u'偶尔（≤3次/周）'),
        (u'经常（≥4次/周）', u'经常（≥4次/周）'),
        (u'一般（少量出汗，心率≤120次/分）', u'一般（少量出汗，心率≤120次/分）'),
        (u'高强度（大汗淋漓，心率>120次/分）', u'高强度（大汗淋漓，心率>120次/分）'),
    )
    # 一级亲属（母亲、姐妹、女儿）异常子宫出血史
    WOMBBLOOD = (
        (u'无', u'无'),
        (u'有', u'有'),
        (u'不详', u'不详'),
    )
    # 是否为排卵障碍性
    OVULATION = (
        (u'是', u'是'),
        (u'否', u'否'),
        (u'不详', u'不详'),
    )

    person = models.OneToOneField(GeneralInfo, related_name='other', on_delete=models.CASCADE)
    owner = models.ForeignKey('myusers.MyUser', related_name='myother', on_delete=models.CASCADE)

    # person_born = models.CharField(verbose_name=u'出生情况', choices=BORNCOND, max_length=30)

    #
    born_zaochan = models.BooleanField(verbose_name="早产", default=False, help_text="早产")
    born_zuyuechan = models.BooleanField(verbose_name="足月产", default=False, help_text="足月产")
    born_yindaofenmian = models.BooleanField(verbose_name="阴道分娩", default=False, help_text="阴道分娩")
    born_pougongchan = models.BooleanField(verbose_name="剖宫产", default=False, help_text="剖宫产")


    # 其它 - 特殊嗜好
    # special_hobbies = models.ForeignKey(OtherSpecialHobbies, on_delete=models.CASCADE)
    hobbies_wu = models.BooleanField(verbose_name=u'无', default=False, help_text="无")
    hobbies_xiyan = models.BooleanField(verbose_name=u'吸烟', default=False, help_text="吸烟")
    hobbies_yinjiu = models.BooleanField(verbose_name=u'饮酒', default=False, help_text="饮酒")
    hobbies_qita = models.CharField(verbose_name=u'其它嗜好', max_length=50, default=u'无', help_text="其他嗜好")

    body_cond = models.CharField(verbose_name=u'体力状况', choices=BODYCOND, max_length=20, help_text="体力状况")
    career_labor = models.CharField(verbose_name=u'职业体力活动', choices=CAREERLABOR, max_length=100, help_text="职业体力活动")
    poor_blood = models.CharField(verbose_name=u'贫血与否', choices=POORBLOOD, max_length=20, help_text="贫血与否")
    phycial_exercise = models.CharField(verbose_name=u'体育锻炼', choices=PHYCIALEXER, max_length=50, help_text="体育锻炼")

    # 其它-减肥情况
    # reduce_fat = models.ForeignKey(OtherReduceFat, on_delete=models.CASCADE)
    reducefat_ever = models.BooleanField(verbose_name=u'有减肥', default=False, help_text="有减肥")
    reducefat_yundong = models.BooleanField(verbose_name=u'运动减肥', default=False, help_text="运动减肥")
    reducefat_jieshi = models.BooleanField(verbose_name=u'节食减肥', default=False, help_text="节食减肥")
    reducefat_yaowu = models.BooleanField(verbose_name=u'药物减肥', default=False, help_text="药物减肥")
    reducefat_qita = models.CharField(verbose_name=u'其它减肥', max_length=50, default=u'无', help_text="其他减肥")
    reducefat_persist = models.IntegerField(verbose_name=u'减肥时长（月）', blank=True, null=True, help_text="减肥时长(月)")

    # 其它-经期情况
    # mens_cond = models.ForeignKey(OtherMensCond, on_delete=models.CASCADE)
    CONDCHOICE = (
        (u'有', u'有'),
        (u'偶尔', u'偶尔'),
        (u'经常', u'经常'),
        (u'无', u'无'),
    )
    mens_yundong = models.CharField(verbose_name=u'经期运动', choices=CONDCHOICE, max_length=10, help_text="经期运动")
    mens_ganmao = models.CharField(verbose_name=u'经期感冒', choices=CONDCHOICE, max_length=10, help_text="经期感冒")
    mens_tongfang = models.CharField(verbose_name=u'经期同房', choices=CONDCHOICE, max_length=10, help_text="经期同房")
    mens_zhaoliang = models.CharField(verbose_name=u'经期着凉', choices=CONDCHOICE, max_length=10, help_text="经期着凉")

    # 其它-平素带下情况
    # leucorrhea = models.ForeignKey(OtherLeucorrhea, on_delete=models.CASCADE)
    leucorrhea_liangshao = models.BooleanField(verbose_name=u'带下量少', default=False, help_text="带下量少")
    leucorrhea_liangke = models.BooleanField(verbose_name=u'带下量可', default=False, help_text="带下量可")
    leucorrhea_liangduo = models.BooleanField(verbose_name=u'带下量多', default=False, help_text="带下量多")
    leucorrhea_sehuang = models.BooleanField(verbose_name=u'带下色黄', default=False, help_text="带下色黄")
    leucorrhea_sebai = models.BooleanField(verbose_name=u'带下色白', default=False, help_text="带下色白")
    leucorrhea_selv = models.BooleanField(verbose_name=u'带下色绿', default=False, help_text="带下色绿")
    leucorrhea_zhiqingxi = models.BooleanField(verbose_name=u'带下质清稀', default=False, help_text="带下质清稀")
    leucorrhea_zhinianchou = models.BooleanField(verbose_name=u'带下质粘稠', default=False, help_text="带下质粘稠")

    # 其它-既往病史
    # past_history = models.ForeignKey(OtherPastHistory, on_delete=models.CASCADE)
    pasthistory_wu = models.BooleanField(verbose_name=u'无', default=False, help_text="无")
    pasthistory_yuejingbutiao = models.BooleanField(verbose_name=u'月经不调', default=False, help_text="月经不调")
    pasthistory_yindaoyan = models.BooleanField(verbose_name=u'阴道炎', default=False, help_text="阴道炎")
    pasthistory_zigongneimoyan = models.BooleanField(verbose_name=u'子宫内膜炎', default=False, help_text="子宫内膜炎")
    pasthistory_zigongneimoyiwei = models.BooleanField(verbose_name=u'子宫内膜异位症', default=False, help_text="子宫内膜异位症")
    pasthistory_zigongxianjizheng = models.BooleanField(verbose_name=u'子宫腺肌症', default=False, help_text="子宫腺肌症")
    pasthistory_penqiangyan = models.BooleanField(verbose_name=u'盆腔炎', default=False, help_text="盆腔炎")
    pasthistory_zigongjiliu = models.BooleanField(verbose_name=u'子宫肌瘤', default=False, help_text="子宫肌瘤")
    pasthistory_luancaonangzhong = models.BooleanField(verbose_name=u'卵巢囊肿', default=False, help_text="卵巢囊肿")
    pasthistory_ruxianzengsheng = models.BooleanField(verbose_name=u'乳腺增生', default=False, help_text="乳腺增生")
    pasthistory_jiazhuangxian = models.BooleanField(verbose_name=u'甲状腺相关疾病', default=False, help_text="甲状腺相关疾病")
    pasthistory_shengzhiyichang = models.BooleanField(verbose_name=u'生殖器官发育异常', default=False, help_text="生殖器发育异常")
    pasthistory_naochuitiliu = models.BooleanField(verbose_name=u'脑垂体瘤', default=False, help_text="脑垂体瘤")
    pasthistory_feipang = models.BooleanField(verbose_name=u'肥胖', default=False, help_text="肥胖")
    pasthistory_ganyan = models.BooleanField(verbose_name=u'肝炎', default=False, help_text="肝炎")
    pasthistory_jiehe = models.BooleanField(verbose_name=u'结核', default=False, help_text="结核")
    pasthistory_qita = models.CharField(verbose_name=u'其它病史', max_length=50, default=u'无', help_text="其他")

    ##############################################################################################
    # 其它-月经不调病史
    # past_mens = models.ForeignKey(OtherPastMenstruation, on_delete=models.CASCADE)
    pastmens_zhouqiwenluan = models.BooleanField(verbose_name=u'月经周期紊乱', default=False, help_text="月经周期紊乱")
    pastmens_liangduo = models.BooleanField(verbose_name=u'月经量多', default=False, help_text="月经量多")
    pastmens_zhouqisuoduan = models.BooleanField(verbose_name=u'月经周期缩短', default=False, help_text="月经周期缩短")
    pastmens_yanhou = models.BooleanField(verbose_name=u'月经延后', default=False, help_text="月经延后")
    pastmens_yanchang = models.BooleanField(verbose_name=u'行经期延长', default=False, help_text="行经期延长")
    pastmens_tingbi = models.BooleanField(verbose_name=u'月经停闭', default=False, help_text="月经停闭")
    pastmens_chuxie = models.BooleanField(verbose_name=u'经间期出血', default=False, help_text="经间期出血")

    womb_blood = models.CharField(verbose_name=u'一级亲属（母亲、姐妹、女儿）异常子宫出血史',
                                  choices=WOMBBLOOD, max_length=10, help_text="一级亲属（母亲、姐妹、女儿）异常子宫出血史")
    ovulation = models.CharField(verbose_name=u'是否为排卵障碍性', choices=OVULATION, max_length=10, help_text="是否为排卵障碍性")
    # 其它-家族史- 一级亲属（父母、兄弟姐妹、子女）其他疾病史
    # past_family = models.ForeignKey(OtherPastFamily, on_delete=models.CASCADE)
    pastfamily_wu = models.BooleanField(verbose_name=u'无', default=False, help_text="无")
    pastfamily_gaoxueya = models.BooleanField(verbose_name=u'高血压', default=False, help_text="高血压")
    pastfamily_tangniaobing = models.BooleanField(verbose_name=u'糖尿病', default=False, help_text="糖尿病")
    pastfamily_xinzangbing = models.BooleanField(verbose_name=u'心脏病', default=False, help_text="心脏病")
    pastfamily_duonangluanchao = models.BooleanField(verbose_name=u'多囊卵巢综合征', default=False, help_text="多囊卵巢综合征")
    pastfamily_buxiang = models.BooleanField(verbose_name=u'不详', default=False, help_text="不详")
    pastfamily_qita = models.CharField(verbose_name=u'其它', max_length=50, default=u'无', help_text="其他")

    # 其它-孕育史
    # past_preg = models.ForeignKey(OtherPastPregnant, on_delete=models.CASCADE)
    pastpreg_yuncount = models.CharField(verbose_name=u'孕次总数', max_length=20, help_text="孕次总数")
    pastpreg_pougong = models.CharField(verbose_name=u'剖宫产次数', blank=True, null=True, max_length=10, help_text="剖宫产次数")
    pastpreg_shunchan = models.CharField(verbose_name=u'顺产次数', blank=True, null=True, max_length=10, help_text="顺产次数")
    pastpreg_yaoliu = models.CharField(verbose_name=u'药物流产次数', blank=True, null=True, max_length=10, help_text="药物流产次数")
    pastpreg_renliu = models.CharField(verbose_name=u'人工流产次数', blank=True, null=True, max_length=10, help_text="人工流产次数")
    pastpreg_ziranliu = models.CharField(verbose_name=u'自然流产次数', blank=True, null=True, max_length=10, help_text="自然流产次数")
    pastpreg_shenghuarenshen = models.CharField(verbose_name=u'生化妊娠次数', blank=True, null=True, max_length=10, help_text="生化妊娠次数")
    pastpreg_yiweirenshen = models.CharField(verbose_name=u'异位妊娠次数', blank=True, null=True, max_length=10, help_text="异位妊娠次数")
    pastpreg_taitingyu = models.CharField(verbose_name=u'胎停育次数', blank=True, null=True, max_length=10, help_text="胎停育次数")
    pastpreg_qinggongshu = models.CharField(verbose_name=u'清宫术次数', blank=True, null=True, max_length=10, help_text="清宫术次数")

    # 其它-避孕措施
    # prevent_method = models.ForeignKey(OtherPrevent, on_delete=models.CASCADE)
    prevent_jieza = models.BooleanField(verbose_name=u'结扎', default=False, help_text="结扎")
    prevent_jieyuqi = models.BooleanField(verbose_name=u'宫内节育器', default=False, help_text="宫内节育器")
    prevent_biyuntao = models.BooleanField(verbose_name=u'避孕套', default=False, help_text="避孕套")
    prevent_biyunyao = models.BooleanField(verbose_name=u'口服避孕药', default=False, help_text="口服避孕药")

    prevent_biyunyao_time = models.DecimalField(verbose_name=u'末次口服避孕药时间', max_digits=3, decimal_places=1, blank=True,
                                        null=True, help_text="末次口服避孕药时间")  # 距离末次性行为之后多长时间服药
    prevent_mafulong = models.BooleanField(verbose_name=u'去氧孕烯炔雌片（妈富隆）', default=False, help_text="去氧孕烯炔雌片（妈富隆）")
    prevent_daying = models.BooleanField(verbose_name=u'炔雌醇环丙孕酮片（达英-35）',
                                         default=False, help_text="炔雌醇环丙孕酮片（达英-35）")
    prevent_yousiming = models.BooleanField(verbose_name=u'屈螺酮炔雌醇片（优思明）',
                                            default=False, help_text="屈螺酮炔雌醇片（优思明）")
    prevent_zuoque = models.BooleanField(verbose_name=u'左炔诺孕酮', default=False, help_text="左炔诺孕酮")
    prevent_fufang = models.BooleanField(verbose_name=u'复方左炔诺孕酮', default=False, help_text="复方左炔诺孕酮")
    prevent_qita = models.CharField(verbose_name=u'其它口服', max_length=100, default=u'无', help_text="其它口服")

    # 其它-辅助性检查
    # accessory_check = models.ForeignKey(OtherAccessoryCheck, on_delete=models.CASCADE)
    HGBVALUE = (
        (u'>110', u'>110'),
        (u'91-110', u'91-110'),
        (u'61-90', u'61-90'),
        (u'30-60', u'30-60'),
    )
    accessory_hgb_value = models.CharField(verbose_name=u'血红蛋白值', choices=HGBVALUE, max_length=20,
                                           blank=True, null=True, help_text="血红蛋白值")
    accessory_quanxuexibaojishu = models.CharField(verbose_name=u'全血细胞计数', max_length=500,
                                                   blank=True, null=True, help_text="全血细胞计数")
    accessory_chuxuexingjibing = models.CharField(verbose_name=u'出血性疾病筛查（如女性血管性血友病）',
                                                  max_length=100, blank=True, null=True, help_text="出血性疾病筛查")
    accessory_ningxue = models.CharField(verbose_name=u'凝血功能检查', max_length=100, blank=True,
                                         null=True, help_text="凝血功能检查")
    accessory_jiazhuangxian = models.CharField(verbose_name=u'甲状腺功能检测',
                                               max_length=100, blank=True, null=True, help_text="甲状腺功能检测")
    accessory_niaorenshen = models.CharField(verbose_name=u'尿妊娠试验', max_length=100, blank=True,
                                             null=True, help_text="尿妊娠试验")
    accessory_penqiangchaosheng = models.CharField(verbose_name=u'盆腔超声检查',
                                                   max_length=100, blank=True, null=True, help_text="盆腔超声检查")
    accessory_jichutiwen = models.CharField(verbose_name=u'基础体温测定', max_length=100, blank=True,
                                            null=True, help_text="基础体温测定")
    accessory_jisushuiping = models.CharField(verbose_name=u'激素水平测定', max_length=100,
                                              blank=True, null=True, help_text="激素水平测定")
    accessory_guagong = models.CharField(verbose_name=u'诊断性刮宫或宫腔镜下刮宫',
                                         max_length=100, blank=True, null=True, help_text="诊断性刮宫或宫腔镜下刮宫")
    accessory_qita = models.CharField(verbose_name=u'其它辅助检查', max_length=100, default=u'无',
                                      blank=True, null=True, help_text="其它辅助检查")

    class Meta:
        verbose_name = u'其它情况'

        verbose_name_plural = verbose_name


################################################################################
# 五、临床诊断
class ClinicalConclusion(models.Model):
    person = models.OneToOneField(GeneralInfo, related_name='clinicalconclusion', on_delete=models.CASCADE)
    owner = models.ForeignKey('myusers.MyUser', related_name='myclinicalconclusion', on_delete=models.CASCADE)

    # 临床诊断-中医诊断
    # chinese_conclusion = models.ForeignKey(ChineseConclusion, on_delete=models.CASCADE)
    benglou = models.BooleanField(verbose_name=u'崩漏', default=False, help_text="崩漏")
    yuejingguoduo = models.BooleanField(verbose_name=u'月经过多', default=False, help_text="月经过多")
    yuejingxianqi = models.BooleanField(verbose_name=u'月经先期', default=False, help_text="月经先期")
    jingqiyanchang = models.BooleanField(verbose_name=u'经期延长', default=False, help_text="经期延长")
    jingjianqichuxie = models.BooleanField(verbose_name=u'经间期出血', default=False, help_text="经间期出血")

    # 临床诊断-辩证分型-虚证
    # asthenic = models.ForeignKey(Asthenic, on_delete=models.CASCADE)
    shenyin = models.BooleanField(verbose_name=u'肾阴虚证', default=False, help_text="肾阴虚证")
    shenyang = models.BooleanField(verbose_name=u'肾阳虚证', default=False, help_text="肾阳虚证")
    shenqi = models.BooleanField(verbose_name=u'肾气虚证', default=False, help_text="肾气虚证")
    piqi = models.BooleanField(verbose_name=u'脾气虚证', default=False, help_text="脾气虚证")
    qixuxiaxian = models.BooleanField(verbose_name=u'气虚下陷证', default=False, help_text="气虚下陷证")
    xure = models.BooleanField(verbose_name=u'虚热证', default=False, help_text="虚热证")
    xinpiliangxu = models.BooleanField(verbose_name=u'心脾两虚证', default=False, help_text="心脾两虚证")
    pishenyangxu = models.BooleanField(verbose_name=u'脾肾阳虚证', default=False, help_text="脾肾阳虚证")
    qixuekuixu = models.BooleanField(verbose_name=u'气血亏虚症', default=False, help_text="气血亏虚症")
    ganshenyinxu = models.BooleanField(verbose_name=u'肝肾阴虚证', default=False, help_text="肝肾阴虚证")
    qita_asthenic = models.CharField(verbose_name=u'其它虚证', max_length=50, default=u'无', help_text="其它虚证")

    # 临床诊断-辩证分型-实证
    # demonstration = models.ForeignKey(Demonstration, on_delete=models.CASCADE)
    ganyuxuere = models.BooleanField(verbose_name=u'肝郁血热证', default=False, help_text="肝郁血热证")
    yangshengxuere = models.BooleanField(verbose_name=u'阳盛血热证', default=False, help_text="阳盛血热证")
    ganjingshire = models.BooleanField(verbose_name=u'肝经湿热证', default=False, help_text="肝经湿热证")
    tanreyuzu = models.BooleanField(verbose_name=u'痰热瘀阻证', default=False, help_text="痰热瘀阻证")
    tanshizuzhi = models.BooleanField(verbose_name=u'痰湿阻滞证', default=False, help_text="痰湿阻滞证")
    tanyuzuzhi = models.BooleanField(verbose_name=u'痰瘀阻滞证', default=False, help_text="痰瘀阻滞证")
    yurehujie = models.BooleanField(verbose_name=u'瘀热互结证', default=False, help_text="瘀热互结证")
    xueyu = models.BooleanField(verbose_name=u'血瘀证', default=False, help_text="血瘀证")
    qizhixueyu = models.BooleanField(verbose_name=u'气滞血瘀证', default=False, help_text="气滞血瘀证")
    hanningxueyu = models.BooleanField(verbose_name=u'寒凝血淤症', default=False, help_text="寒凝血淤症")
    qita_demonstration = models.CharField(verbose_name=u'其它实证', max_length=50, default=u'无', help_text="其它实证")

    # 临床诊断-辩证分型-虚实夹杂证
    # deficiency_excess = models.ForeignKey(DeficiencyExcess, on_delete=models.CASCADE)
    shenxuxueyu = models.BooleanField(verbose_name=u'肾虚血瘀证', default=False, help_text="肾虚血瘀证")
    shenxuyure = models.BooleanField(verbose_name=u'肾虚瘀热证', default=False, help_text="肾虚瘀热证")
    shenxuganyu = models.BooleanField(verbose_name=u'肾虚肝郁证', default=False, help_text="肾虚肝郁证")
    qixuxueyu = models.BooleanField(verbose_name=u'气虚血瘀证', default=False, help_text="气虚血瘀证")
    yinxuxueyu = models.BooleanField(verbose_name=u'阴虚血瘀证', default=False, help_text="阴虚血瘀证")
    yinxuhuowang = models.BooleanField(verbose_name=u'阴虚火旺证', default=False, help_text="阴虚火旺证")
    ganyupixu = models.BooleanField(verbose_name=u'肝郁脾虚证', default=False, help_text="肝郁脾虚证")
    qita_def_ex = models.CharField(verbose_name=u'其它虚实', max_length=50, default=u'无', help_text="其它虚实")

    # 临床诊断-西医诊断
    # west_conclusion = models.ForeignKey(WestConclusion, on_delete=models.CASCADE)
    duonangluanchao = models.BooleanField(verbose_name=u'多囊卵巢综合征', default=False, help_text="多囊卵巢综合征")
    gaomirusu = models.BooleanField(verbose_name=u'高泌乳素血症', default=False, help_text="高泌乳素血症")
    dicuxingxianjisu = models.BooleanField(verbose_name=u'低促行线激素疾病', default=False, help_text="低促行线激素疾病")
    qita_west = models.CharField(verbose_name=u'其它西医诊断', max_length=50, default=u'无', help_text="其它西医诊断")

    class Meta:
        verbose_name = u'临床诊断'

        verbose_name_plural = verbose_name


################################################################################
# 六、文件上传
from myusers.models import MyUser


class InvestFileUpload(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=10, help_text="名称")
    ivfile = models.FileField(verbose_name=u'文件地址', upload_to='avatars/%Y-%m-%d/%H-%M',
                              default="/avatars/default.xlsx", help_text="文件地址")
    owner = models.ForeignKey(MyUser, related_name='myinvestfileupload', on_delete=models.CASCADE, help_text="用户")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'上传文件'
        verbose_name_plural = verbose_name

