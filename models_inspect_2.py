# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acknowledgementreceived(models.Model):
    a_id = models.IntegerField(db_column='A_ID', primary_key=True)  # Field name made lowercase.
    r = models.ForeignKey('Acknowledgementrequest', models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.
    msgfile = models.BinaryField(db_column='MsgFile', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcknowledgementReceived'


class Acknowledgementrequest(models.Model):
    r_id = models.IntegerField(db_column='R_ID', primary_key=True)  # Field name made lowercase.
    cnr = models.ForeignKey('Creditnoteresumeemail', models.DO_NOTHING, db_column='CNR_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    senddate = models.DateTimeField(db_column='SendDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcknowledgementRequest'


class Creditnoteresumeemail(models.Model):
    cnr_id = models.IntegerField(db_column='CNR_ID', primary_key=True)  # Field name made lowercase.
    cn_id = models.CharField(db_column='CN_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dateissued = models.DateTimeField(db_column='DateIssued', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    body = models.TextField(db_column='Body', blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=40, blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.BooleanField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditNoteResumeEmail'


class Creditnotes(models.Model):
    cn_id = models.CharField(db_column='CN_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    d_id = models.CharField(db_column='D_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    totaldocumentamount = models.DecimalField(db_column='TotalDocumentAmount', max_digits=38, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    totalvatamountdocumentt = models.DecimalField(db_column='TotalVATAmountDocumentt', max_digits=38, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    totaldocumentamountwithvat = models.DecimalField(db_column='TotalDocumentAmountWithVAT', max_digits=38, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    accountingnumberid = models.CharField(db_column='AccountingNumberID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    issueddate = models.DateTimeField(db_column='IssuedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditNotes'


class Dealers(models.Model):
    d_id = models.CharField(db_column='D_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    dealername = models.CharField(db_column='DealerName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dealervatnumber = models.CharField(db_column='DealerVATnumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dealeremail = models.CharField(db_column='DealerEmail', max_length=80, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Dealers'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
