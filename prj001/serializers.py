from rest_framework import serializers
from myusers.models import MyUser
from .models import GeneralInfo, Menstruation, Symptom, Other, ClinicalConclusion
from .models import InvestFileUpload

from .utils import validate_file
from .utils import validate_person


#######################################################################
class MyUserGenInfoDetailSerializer(serializers.ModelSerializer):
    # generalinfo = serializers.HyperlinkedRelatedField(many=True, view_name='generalinfo-detail', read_only=True)
    # mygi = serializers.StringRelatedField(many=True)
    mygi = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='generalinfo-detail'
    )

    class Meta:
        model = MyUser
        fields = ('url', 'email', 'user_name','mygi')


#######################################################################
class GeneralInfoListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = GeneralInfo
        fields = ('url', 'owner', 'id', 'serial', 'name', 'age', 'height', 'weight', 'blood_type', 'nation')


class GeneralListSerializer(serializers.ModelSerializer):
    """
    信息列表序列化器
    """
    menstruation = serializers.HyperlinkedRelatedField(label="",
                                                       read_only=True,
                                                       view_name='menstruation-detail')
    symptom = serializers.HyperlinkedRelatedField(label="",
                                                  read_only=True,
                                                  view_name='symptom-detail')
    other = serializers.HyperlinkedRelatedField(label="其他",
                                                read_only=True,
                                                view_name='other-detail')
    clinicalconclusion = serializers.HyperlinkedRelatedField(label="",
                                                             read_only=True,
                                                             view_name='clinicalconclusion-detail')

    class Meta:
        model = GeneralInfo

        fields = ("url", "id", "menstruation", "other", "clinicalconclusion",
                  "symptom", "name", "nation", "age", "height", "weight",
                  "blood_type", "culture", "marriage", "career", "owner_id")


class GeneralInfoCreateSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = GeneralInfo
        fields = ('url', 'owner', 'id', 'recdate', 'serial', 'hospital', 'expert', 'title', 'name', 'telephone', 'age',
                  'height', 'weight', 'blood_type', 'nation', 'career',
                  'gaokong', 'diwen', 'zaosheng', 'fushe', 'huagongyinran', 'julieyundong', 'qiyou', 'wu',
                  'address', 'entrance', 'culture', 'marriage',
                  'wuteshu', 'sushi', 'suan', 'tian', 'xian', 'xinla', 'you', 'shengleng', 'kafei', 'qita')


class GeneralInfoDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    menstruation = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='menstruation-detail'
    )

    symptom = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='symptom-detail'
    )

    other = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='other-detail'
    )

    clinicalconclusion = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='clinicalconclusion-detail'
    )

    class Meta:
        model = GeneralInfo
        fields = ('url', 'owner', 'id', 'recdate', 'serial', 'hospital', 'expert', 'title', 'name', 'telephone', 'age',
                  'height', 'weight', 'blood_type', 'nation', 'career',
                  'gaokong', 'diwen', 'zaosheng', 'fushe', 'huagongyinran', 'julieyundong', 'qiyou', 'wu',
                  'address', 'entrance', 'culture', 'marriage',
                  'wuteshu', 'sushi', 'suan', 'tian', 'xian', 'xinla', 'you', 'shengleng', 'kafei', 'qita',
                  'menstruation', 'symptom', 'other', 'clinicalconclusion')

    # def create(self, validated_data):
    #     gispecenv_data = validated_data.pop('gispecenv')
    #     gieathobbies_data = validated_data.pop('gieathobbies')
    #     gi = GeneralInfo.objects.create(**validated_data)
    #     GeneralSpecEnv.objects.create(person=gi, **gispecenv_data)
    #     GeneralEatHobbies.objects.create(person=gi, **gieathobbies_data)
    #     return gi


class GeneralInfoPageSeriaializer(serializers.Serializer):
    """分页请求序列化器"""
    page = serializers.IntegerField(label="当前页")

    def validate(self, data):
        page = data.get("page", 0)

        if not page:
            raise serializers.ValidationError("参数未传递")
        return data


class GeneralInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralInfo

        fields = "__all__"


class MenstruationSerializer(serializers.ModelSerializer):
    # person_id = serializers.IntegerField(label="一般信息的外键",
    #                                      write_only=True,
    #                                      help_text="一般信息的ID")

    class Meta:
        model = Menstruation
        fields = "__all__"
        extra_kwargs = {
            "owner": {
               "read_only": True
            },
            "person": {
                "help_text": "患者ID"
            }
        }

    def validate(self, data):
        """
        验证 person_id
        :param data:
        :return:
        """
        return validate_person(self, GeneralInfo, Menstruation, data)


class SymptomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptom
        fields = "__all__"
        extra_kwargs = {
            "owner": {
                "read_only": True
            },
            "person": {
                "help_text": "患者ID"
            }
        }

    def validate(self, data):
        return validate_person(self, GeneralInfo, Symptom, data)


class OtherSerializer(serializers.ModelSerializer):

    HGBVALUE = [
        u'>110',u'91-110',u'61-90',u'30-60'
    ]
    # accessory_hgb_value = serializers.ChoiceField(choices=HGBVALUE, help_text=u'血红蛋白值')
    # accessory_hgb_value = serializers.CharField(help_text=u'血红蛋白值')

    class Meta:
        model = Other
        fields = "__all__"
        extra_kwargs = {
            "owner": {
                "read_only": True
            },
            "person": {
                "help_text": "患者ID"
            }
        }

    def validate(self, data):
        return validate_person(self, GeneralInfo, Other, data)


class ClinicalConclusionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClinicalConclusion
        fields = "__all__"
        extra_kwargs = {
            "owner": {
                "read_only": True
            },
            "person": {
                "help_text": "患者ID"
            }
        }

    def validate(self, data):
        return validate_person(self, GeneralInfo, ClinicalConclusion, data)


class InvestFileUploadSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(label="所属者", read_only=True)

    ivfile = serializers.FileField(max_length=None,
                                   allow_empty_file=False,
                                   help_text="选择上传文件",)
    name = serializers.CharField(max_length=50,
                                 help_text="文件描述",
                                 allow_blank=False,
                                 write_only=True)

    class Meta:
        model = InvestFileUpload
        # fields = "__all__"
        fields = ("id", "name", "ivfile", "owner_id")

    def validate(self, data):
        return validate_file(data)


# 保存数据库的多表序列化器
class InfoSerializer(serializers.Serializer):
    clinicalconclusion = ClinicalConclusionSerializer()
    other = OtherSerializer()
    symptom = SymptomSerializer()
    menstruation = MenstruationSerializer()

    class Meta:
        model = GeneralInfo
        fields = "__all__"


