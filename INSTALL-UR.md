# MRK Blogger Theme — اردو ہدایات

بلاگ: https://mrkdigitalservices.blogspot.com/

## GitHub پر خودکار جانچ
تھیم یا validation فائل میں تبدیلی commit ہونے پر GitHub Actions خود بخود:
1. XML کی ساخت چیک کرتا ہے۔
2. Blogger کے skin اور widget sections کی موجودگی چیک کرتا ہے۔
3. widget/section IDs میں خالی یا دہرائی گئی قدریں تلاش کرتا ہے۔
4. کامیاب جانچ پر XML فائل کا artifact تیار کرتا ہے اور Actions run میں خلاصہ لکھتا ہے۔

ورک فلو: https://github.com/Meelad5815/BlogSpot-/actions

## اہم حد
یہ جانچ Blogger کے اپنے سرور پر ہونے والی مکمل template validation نہیں ہے۔ اس سے یہ ضمانت نہیں ملتی کہ Blogger تھیم قبول کر لے گا، اور یہ workflow لائیو ویب سائٹ پر تھیم اپ لوڈ نہیں کرتا۔

Blogger API v3 میں پوسٹس اور صفحات کے لیے API موجود ہے، لیکن تھیم اپ لوڈ/اپ ڈیٹ کرنے کا کوئی دستاویزی عوامی endpoint موجود نہیں۔ اس لیے GitHub Secrets میں OAuth token رکھنے سے تھیم کی خودکار اپ لوڈ خود بخود ممکن نہیں ہو جاتی۔

## سکیورٹی
- Google password، session cookie یا token کو README، عام ڈاکیومنٹ، XML فائل یا Git commit میں نہ ڈالیں۔
- GitHub Secrets صرف اس وقت استعمال کریں جب کوئی واضح، دستیاب API action واقعی اس credential کی ضرورت رکھتا ہو۔
- کسی نامعلوم deployment script کو Google credentials نہ دیں۔

## لائیو تھیم لگانے سے پہلے
1. Blogger میں موجودہ تھیم کا backup بنائیں۔
2. GitHub Actions کی validation مکمل ہونے دیں۔
3. Blogger کے Theme حصے سے منظور شدہ XML اپ لوڈ کریں۔
4. موبائل اور کمپیوٹر پر ویب سائٹ چیک کریں اور خرابی ہو تو backup بحال کریں۔

## تھیم فائل
https://github.com/Meelad5815/BlogSpot-/blob/main/theme/mrk-blogger-theme.xml
