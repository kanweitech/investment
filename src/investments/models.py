import uuid
from decimal import Decimal
from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator
from django.db.models import base
from django.utils.translation import ugettext_lazy as _

from acctmang.models import User




class Investments(models.Model):
    class Meta:
        verbose_name = "investment"
        verbose_name_plural = "investments"
        db_table = 'investments'


    STATUS = (
        ('Pending', 'Pending'), 
        ('Active', 'Active'),
        ('Complete', 'Complete'),)

    uid = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=1000, null=True, blank=True, editable=False) # Fallback for investment_plan
    investment_plan= models.ForeignKey("InvestmentPlan", on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0.00")),
        ],)
    investor = models.CharField(max_length=1000, editable=False) # Fallback for user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start = models.CharField(max_length=1000, null=True, blank=True, editable=False) # Fallback for startdate
    startdate = models.DateField(blank=True, null=True)
    """
    Start Date is updated when admin activates investment plan. The previous `start` date string was stored without proper parsing.
    It strives to follow a Date Format: %d %b %Y %H:%M:%S %p. But fails a thorough check. Fall back fields will be archived" 
    """
    end = models.CharField(max_length=1000, null=True, blank=True, editable=False) # Fallback for enddate
    enddate = models.DateField(blank=True, null=True)
    """
    End Date is updated when admin submits investor for Capital + ROI returns
    """
    roi = models.CharField(max_length=1000, null=True) # Fallback for roi_metadata
    roi_metadata = models.JSONField(default=dict, help_text="This Contains breakdown of the Current ROI percentage during creation and the expected Returns")
    """
    ROI MetaData Format:
    {
        amount: decimal e.g 100000.00
        current_roi_percentage: decimal e.g 40.00 | 22.57 etc,
        expected_capital_gain: 50000.00
        expected_return: decimal e.g 150000.00,
    }

    Query Method:
        Querying a User's Investment requires query method to take into consideration the backward compatibility 
        of the system. If a user has a filled roi_metadata then the user was created on this system. Otherwise we will
        fallback to the `roi` field.
    """
    status = models.CharField(max_length=1000, choices=STATUS, default="Pending")
    unit = models.IntegerField()
    created= models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now_add=True)


class InvestmentPlan(models.Model):

    plan_id = models.UUIDField(default=uuid.uuid4)
    name  = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from='name')
    unit_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0.00")),
        ],help_text="Price for a unit of this plan")

    roi_percentage = models.DecimalField(
        _("Roi"),
        default=0,
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0.00")),
        ],
        help_text="Percentage Value for ROI e.g 50, 10.6, 4.99 etc.", )
    
    image_url = models.URLField()

    created= models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return str(self.plan_id)



