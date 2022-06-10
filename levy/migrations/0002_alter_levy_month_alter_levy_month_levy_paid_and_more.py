# Generated by Django 4.0.1 on 2022-04-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levy',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default=2022, max_length=100),
        ),
        migrations.AlterField(
            model_name='levy',
            name='month_levy_paid',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='levy',
            name='year',
            field=models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022),
        ),
        migrations.AlterUniqueTogether(
            name='levy',
            unique_together={('year', 'month')},
        ),
    ]
