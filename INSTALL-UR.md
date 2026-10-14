# MRK Blogger Theme — تنصیب کی ہدایات

بلاگ: https://mrkdigitalservices.blogspot.com/

## GitHub میں تھیم تبدیل کرنا
1. فائل کھولیں: https://github.com/Meelad5815/BlogSpot-/blob/main/theme/mrk-blogger-theme.xml
2. تبدیلی کریں اور Commit changes کریں۔
3. GitHub Actions میں Validate Blogger theme XML ورک فلو مکمل ہونے دیں۔
4. کامیاب ہونے پر Actions run کی Artifacts فہرست سے mrk-blogger-theme ZIP حاصل کریں، یا XML فائل براہ راست ڈاؤن لوڈ کریں۔

## Blogger میں تھیم لگانا
1. Blogger کھولیں اور درست بلاگ منتخب کریں۔
2. Theme مینو سے موجودہ تھیم کا Backup ڈاؤن لوڈ کریں۔
3. Theme مینو میں Restore منتخب کرکے نئی XML فائل اپ لوڈ کریں۔
4. موبائل اور کمپیوٹر پر چیک کریں۔ مسئلہ ہو تو Backup بحال کریں۔

## خودکار اپ ڈیٹ کی حد
GitHub commit سے Blogger کی live تھیم خودکار طور پر تبدیل نہیں ہوتی۔ Blogger API v3 میں theme upload/update endpoint موجود نہیں؛ موجودہ workflow XML کی جانچ کرتا ہے۔ live تبدیلی کے لیے Blogger میں Restore کے ذریعے فائل اپ لوڈ کرنا ضروری ہے۔ OAuth tokens یا passwords کو repository میں محفوظ نہ کریں۔