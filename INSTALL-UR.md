# MRK Blogger Theme — اردو ہدایات

بلاگ: https://mrkdigitalservices.blogspot.com/

## تیار XML تھیم ڈاؤن لوڈ کریں
- **براہِ راست XML فائل:** https://raw.githubusercontent.com/Meelad5815/BlogSpot-/main/theme/mrk-blogger-theme.xml
- GitHub پر فائل دیکھیں: https://github.com/Meelad5815/BlogSpot-/blob/main/theme/mrk-blogger-theme.xml
- تمام تصویری اثاثے: https://github.com/Meelad5815/BlogSpot-/tree/main/assets

## تھیم لگانے کا طریقہ
1. Blogger ڈیش بورڈ کھولیں: https://www.blogger.com/
2. **Theme** پر جائیں۔
3. موجودہ تھیم کا **Backup/Download** ضرور بنائیں، تاکہ مسئلہ ہونے پر واپس بحال کر سکیں۔
4. Theme کے مینو میں **Restore** یا **Upload** کا اختیار کھولیں (Blogger کے انٹرفیس میں نام بدل سکتا ہے)۔
5. ڈاؤن لوڈ کی ہوئی `mrk-blogger-theme.xml` فائل منتخب کریں اور اپ لوڈ مکمل ہونے دیں۔
6. ویب سائٹ کو موبائل اور کمپیوٹر دونوں پر کھول کر Home، Services، About، Contact، پوسٹس، سرچ اور تصویریں چیک کریں۔

اگر آپ XML کوڈ کھول کر کاپی کرنا چاہیں تو براہِ راست XML لنک کھولیں، پورا کوڈ کاپی کر کے UTF-8 انکوڈنگ کے ساتھ `mrk-blogger-theme.xml` کے نام سے محفوظ کریں۔ بہتر طریقہ یہ ہے کہ فائل ڈاؤن لوڈ کریں، تاکہ کوڈ ادھورا کاپی نہ ہو۔

## تصاویر کیسے آئیں گی؟
تھیم میں تصاویر کے مکمل HTTPS لنکس شامل ہیں۔ تصویر کی اصل فائل XML کے اندر نہیں بلکہ GitHub کے `assets/` فولڈر میں موجود ہے؛ تھیم ان لنکس سے تصویر دکھاتا ہے۔ اس لیے XML اکیلی فائل میں لے آنا کافی ہے، بشرطیکہ GitHub repository اور asset links دستیاب رہیں۔ اگر repository یا فائلوں کے نام/مقام بدلیں تو XML میں متعلقہ لنکس بھی بدلنے ہوں گے۔ بلاگ پوسٹس کے اندر شامل تصاویر الگ سے پوسٹ کے مواد میں رہتی ہیں؛ یہ تھیم موجودہ پوسٹس کے متن یا تصاویر کو خودکار طور پر تبدیل نہیں کرتا۔

## خودکار جانچ اور اس کی حد
ورک فلو: https://github.com/Meelad5815/BlogSpot-/actions

GitHub Actions XML well-formedness، Blogger skin، sections، widget IDs اور widget types کی static جانچ کرتا ہے۔ یہ Blogger کے سرور پر اصل اپ لوڈ نہیں کرتا، اور static جانچ اس بات کی ضمانت نہیں کہ Blogger ہر template rule قبول کرے گا۔ Blogger API v3 میں تھیم اپ لوڈ/اپ ڈیٹ کرنے کا دستاویزی عوامی endpoint موجود نہیں؛ اس لیے لائیو انسٹالیشن Blogger کے Theme انٹرفیس سے کرنی ہوگی۔

## سکیورٹی
- Google password، session cookie یا OAuth token کو XML، README، عام فائل یا Git commit میں کبھی شامل نہ کریں۔
- کسی غیر تصدیق شدہ script کو Google credentials نہ دیں۔
- مسئلہ ہو تو پہلے بنایا ہوا backup بحال کریں۔
