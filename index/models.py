from django.db import models
from django.utils.text import slugify


class Upload(models.Model):
    title = models.CharField(max_length=512)
    file = models.FileField()
    ip = models.CharField(max_length=128)
    agent = models.CharField(max_length=512)
    slug = models.SlugField(max_length=40, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Upload, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'upload'
        verbose_name_plural = 'uploads'

    def __str__(self):
        return self.title


class Pages(models.Model):
    title = models.CharField(max_length=512)
    body = models.CharField(max_length=2048)
    pic = models.FileField()

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.title


class Link(models.Model):
    ACTIVE = '1'
    DISABLE = '0'
    STATUS = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    ENGLISH = 'EN'
    PERSIAN = 'FA'
    LANGUAGE = (
        (ENGLISH, 'English'),
        (PERSIAN, 'Persian'),
    )
    TEXT_LINK = 'T'
    IMG_LINK = 'I'
    THUMB_LINK = 'H'
    TYPE = (
        (TEXT_LINK, 'Text-Link'),
        (IMG_LINK, 'Img-Link'),
        (THUMB_LINK, 'Thumb-Link'),
    )
    title = models.CharField(max_length=512)
    body = models.CharField(max_length=2048)
    pic = models.FileField()
    file = models.FileField()
    status = models.CharField(max_length=1, choices=STATUS, default=ACTIVE, )
    type = models.CharField(max_length=1, choices=TYPE, default=TEXT_LINK, )
    link = models.TextField()
    lang = models.CharField(max_length=2, choices=LANGUAGE, default=PERSIAN, )

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.title


class Message(models.Model):
    ACTIVE = '1'
    DISABLE = '0'
    STATUS = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    ACTIVE = '1'
    DISABLE = '0'
    FAQ = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    ENGLISH = 'EN'
    PERSIAN = 'FA'
    LANGUAGE = (
        (ENGLISH, 'English'),
        (PERSIAN, 'Persian'),
    )
    CONTACT_US = 'CU'
    P2P = 'PP'
    BROADCAST = 'BC'
    SUPPORT = 'ST'
    TYPE = (
        (CONTACT_US, 'Contact Us'),
        (P2P, 'person to person'),
        (BROADCAST, 'Broadcast'),
        (SUPPORT, 'support'),
    )
    name = models.CharField(max_length=512)
    title = models.CharField(max_length=512)
    answer = models.CharField(max_length=512)
    parent = models.CharField(max_length=512)
    faq = models.CharField(max_length=1, choices=FAQ, default=ACTIVE, )
    chat_id = models.CharField(max_length=512, null=True, blank=True)
    user_id = models.CharField(max_length=512, null=True, blank=True)
    phone = models.FloatField()
    mail = models.EmailField()
    date_time = models.TimeField()
    ip = models.CharField(max_length=128)
    agent = models.CharField(max_length=512)
    read = models.CharField(max_length=1024)
    body = models.CharField(max_length=2048)
    status = models.CharField(max_length=1, choices=STATUS, default=ACTIVE, )
    type = models.CharField(max_length=1, choices=TYPE, default=CONTACT_US, )
    link = models.TextField()
    lang = models.CharField(max_length=2, choices=LANGUAGE, default=PERSIAN, )

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    ACTIVE = '1'
    DISABLE = '0'
    STATUS = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    ENGLISH = 'EN'
    PERSIAN = 'FA'
    LANGUAGE = (
        (ENGLISH, 'English'),
        (PERSIAN, 'Persian'),
    )

    name = models.CharField(max_length=512)
    pic = models.FileField()
    status = models.CharField(max_length=1, choices=STATUS, default=ACTIVE, )
    link = models.TextField()
    lang = models.CharField(max_length=2, choices=LANGUAGE, default=PERSIAN, )

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'

    def __str__(self):
        return self.name


class Content(models.Model):
    ACTIVE = '1'
    DISABLE = '0'
    STATUS = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    ENGLISH = 'EN'
    PERSIAN = 'FA'
    LANGUAGE = (
        (ENGLISH, 'English'),
        (PERSIAN, 'Persian'),
    )

    title = models.CharField(max_length=512)
    v_c = models.CharField(max_length=11)
    ttr = models.TimeField(max_length=8)
    ip = models.CharField(max_length=128)
    status = models.CharField(max_length=1, choices=STATUS, default=ACTIVE, )
    desc = models.CharField(max_length=2048)
    body = models.CharField(max_length=2048)
    date = models.CharField(max_length=10)
    lang = models.CharField(max_length=2, choices=LANGUAGE, default=PERSIAN, )

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

    def __str__(self):
        return self.title


class Workshop(models.Model):
    DIPLOM = '0'
    LISANS = '1'
    FOGHLISANS = '2'
    DOC = '3'
    FOGHDOC = '4'
    FREE = '5'
    LAST_DEGREE = (
        (DIPLOM, 'Active'),
        (LISANS, 'Disabled'),
        (FOGHLISANS, 'Disabled'),
        (DOC, 'Disabled'),
        (FOGHDOC, 'Disabled'),
        (FREE, 'Disabled'),
    )
    ENGLISH = 'EN'
    PERSIAN = 'FA'
    LANGUAGE = (
        (ENGLISH, 'English'),
        (PERSIAN, 'Persian'),
    )

    name = models.CharField(max_length=512)
    family = models.CharField(max_length=512)
    last_degree = models.CharField(max_length=2, choices=LAST_DEGREE, default=FREE, )
    major = models.CharField(max_length=512)
    institute = models.CharField(max_length=512)
    expertise = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    mail = models.EmailField()
    phone = models.CharField(max_length=11)
    tools = models.CharField(max_length=512)
    time = models.TimeField
    point = models.CharField(max_length=512)
    pic = models.FileField()

    class Meta:
        verbose_name = 'Workshop'
        verbose_name_plural = 'Workshops'

    def __str__(self):
        return self.name


class Register(models.Model):
    DIPLOM = '0'
    LISANS = '1'
    FOGHLISANS = '2'
    DOC = '3'
    FOGHDOC = '4'
    FREE = '5'
    LAST_DEGREE = (
        (DIPLOM, 'Active'),
        (LISANS, 'Disabled'),
        (FOGHLISANS, 'Disabled'),
        (DOC, 'Disabled'),
        (FOGHDOC, 'Disabled'),
        (FREE, 'Disabled'),
    )
    ENGLISH = 'EN'
    PERSIAN = 'FA'
    LANGUAGE = (
        (ENGLISH, 'English'),
        (PERSIAN, 'Persian'),
    )
    VALIDATE = 'V'
    UNVALIDATE = 'U'
    STATUS = (
        (VALIDATE, 'Validate'),
        (UNVALIDATE, 'unvalidate'),
    )
    PAID = 'V'
    UNPAID = 'U'
    WATING = 'U'
    PAY_STATUS = (
        (PAID, 'Validate'),
        (UNPAID, 'unvalidate'),
        (WATING, 'unvalidate'),
    )
    TEXT_LINK = 'T'
    IMG_LINK = 'I'
    THUMB_LINK = 'H'
    TYPE = (
        (TEXT_LINK, 'Text-Link'),
        (IMG_LINK, 'Img-Link'),
        (THUMB_LINK, 'Thumb-Link'),
    )
    ACTIVE = '1'
    DISABLE = '0'
    MAIL = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    name = models.CharField(max_length=512)
    family = models.CharField(max_length=512)
    last_degree = models.CharField(max_length=2, choices=LAST_DEGREE, default=FREE, )
    major = models.CharField(max_length=512)
    institute = models.CharField(max_length=512)
    nationality = models.CharField(max_length=512)
    expertise = models.CharField(max_length=512)
    state = models.CharField(max_length=512)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=512)
    postal_code = models.CharField(max_length=512)
    phone = models.CharField(max_length=11)
    mobile = models.CharField(max_length=11)
    fax = models.CharField(max_length=11)
    username = models.CharField(max_length=11)
    password = models.CharField(max_length=11)
    mail = models.EmailField()
    mail_verify = models.EmailField(max_length=1, choices=MAIL, default=ACTIVE)
    tracking_code = models.CharField(max_length=512)
    agent = models.CharField(max_length=512)
    ip = models.CharField(max_length=128)
    registration_date = models.CharField(max_length=256)
    pic = models.FileField()
    point = models.CharField(max_length=512)
    pay_id = models.CharField(max_length=11)
    pay_sts = models.CharField(max_length=1, choices=PAY_STATUS, default=WATING)
    scan_id = models.CharField(max_length=11)
    scan_bc = models.CharField(max_length=10)
    document_validation_sts = models.CharField(max_length=1, choices=STATUS, default=VALIDATE)
    type = models.CharField(max_length=1, choices=TYPE, default=TEXT_LINK)

    class Meta:
        verbose_name = 'Register'
        verbose_name_plural = 'Registers'

    def __str__(self):
        return self.name


class Language(models.Model):
    ACTIVE = '1'
    DISABLE = '0'
    STATUS = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    title = models.CharField(max_length=512)
    status = models.CharField(max_length=1, choices=STATUS, default=ACTIVE)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.title


class Payment(models.Model):
    PAID = 'V'
    UNPAID = 'U'
    WATING = 'U'
    ERROR = 'E'
    STATUS = (
        (PAID, 'paid'),
        (UNPAID, 'unpaid'),
        (WATING, 'wating'),
        (ERROR, 'error'),
    )
    ACTIVE = '1'
    DISABLE = '0'
    STATUS = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    VER_STATUS = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    user_id = models.CharField(max_length=512)
    articte_id = models.CharField(max_length=512)
    amount = models.CharField(max_length=10)
    ref_num = models.CharField(max_length=20)
    res_num = models.CharField(max_length=20)
    verified = models.CharField(max_length=1, choices=VER_STATUS, default=ACTIVE)
    status = models.CharField(max_length=1, choices=STATUS, default=WATING)
    date_time = models.TimeField()
    ip = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.user_id


class Setting(models.Model):
    ACTIVE = '1'
    UNDERCRUSTION = '0'
    COMING_SOON = '1'
    DISABLED = '2'
    SITE_STS = (
        (ACTIVE, 'Active'),
        (UNDERCRUSTION, 'under crustion'),
        (COMING_SOON, 'coming soon'),
        (DISABLED, 'Disabled'),
    )
    VER_STATUS = (
        (ACTIVE, 'Active'),
        (DISABLED, 'Disabled'),
    )
    ACTIVE = '1'
    DISABLE = '0'
    E_STS = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    ACTIVE = '1'
    DISABLE = '0'
    SMS_STS = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    INTAGRAM = '1'
    TWIETER = '2'
    FACEBOOK = '3'
    SOCIAL = (
        (INTAGRAM, 'Instagram'),
        (TWIETER, 'Twieter'),
        (FACEBOOK, 'Facebook'),
    )

    website_url = models.CharField(max_length=512)
    domain = models.CharField(max_length=512)
    keyword_fa = models.CharField(max_length=512)
    keyword_en = models.CharField(max_length=512)
    desc_en = models.CharField(max_length=512)
    desc_fa = models.CharField(max_length=512)
    title_fa = models.CharField(max_length=512)
    title_en = models.CharField(max_length=512)
    e_ip = models.CharField(max_length=512)
    e_u = models.CharField(max_length=512)
    e_p = models.CharField(max_length=512)
    e_ssl = models.CharField(max_length=512)
    e_port = models.CharField(max_length=512)
    e_name = models.CharField(max_length=512)
    e_sts = models.CharField(max_length=1, choices=E_STS, default=ACTIVE)
    sms_line = models.CharField(max_length=512)
    sms_u = models.CharField(max_length=512)
    sms_p = models.CharField(max_length=512)
    sms_domain = models.CharField(max_length=512)
    sms_method = models.CharField(max_length=512)
    sms_sts = models.CharField(max_length=1, choices=SMS_STS, default=ACTIVE)
    tg_channel = models.CharField(max_length=512)
    tg_chat_person = models.CharField(max_length=512)
    tg_chat_bot = models.CharField(max_length=512)
    tg_bot_token_a = models.CharField(max_length=512)
    tg_bot_token_b = models.CharField(max_length=512)
    tg_bot_user = models.CharField(max_length=512)
    site_sts = models.CharField(max_length=1, choices=SITE_STS, default=ACTIVE)
    author_en = models.CharField(max_length=512)
    author_fa = models.CharField(max_length=512)
    copyright_en = models.CharField(max_length=512)
    copyright_fa = models.CharField(max_length=512)
    countdown = models.CharField(max_length=512)
    map = models.CharField(max_length=512)
    logo_en = models.CharField(max_length=512)
    logo_fa = models.CharField(max_length=512)
    footer_en = models.CharField(max_length=512)
    footer_fa = models.CharField(max_length=512)
    footer_logo = models.CharField(max_length=512)
    social = models.CharField(max_length=1, choices=SOCIAL, default=FACEBOOK)

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.website_url


class Articles(models.Model):
    ACTIVE = '1'
    DISABLE = '0'
    PAY_STS = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )
    Posted_to_the_secretariat = '1'
    Send_to_the_referee = '2'
    Under_review_by_the_referee = '3'
    failed = '4'
    Accept = '5'
    STATUS = (
        (Posted_to_the_secretariat, 'Posted_to_the_secretariat'),
        (Send_to_the_referee, 'Send_to_the_referee'),
        (Under_review_by_the_referee, 'Under_review_by_the_referee'),
        (failed, 'failed'),
        (Accept, 'Accept'),
    )

    title = models.CharField(max_length=512)
    desc = models.CharField(max_length=512)
    authors = models.CharField(max_length=512)
    speaker = models.CharField(max_length=512)
    file = models.CharField(max_length=512)
    id_author = models.CharField(max_length=512)
    pay_sts = models.CharField(max_length=1, choices=PAY_STS, default=ACTIVE)
    pay_id = models.CharField(max_length=512)
    status = models.CharField(max_length=1, choices=STATUS, default=Under_review_by_the_referee)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

# davar + emtiaz + comments
