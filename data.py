import pandas as pd

data = [
    {
        "id": 1,
        "name": "Apple iPhone 12",
        "description": "The Apple iPhone 12 features a 6.1-inch Super Retina XDR display and A14 Bionic chip.",
        "price": 999.00,
        "category": "Electronics",
        "image": "https://www.apple.com/newsroom/images/product/iphone/standard/Apple_iPhone-12_red-product(1)_10132020_big.jpg.large.jpg"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S21",
        "description": "The Samsung Galaxy S21 features a 6.2-inch Dynamic AMOLED display and Exynos 2100 chip.",
        "price": 799.00,
        "category": "Electronics",
        "image": "https://images.samsung.com/is/image/samsung/p6pim/in/sm-g991bzviinu/gallery/in-galaxy-s21-5g-g991-sm-g991bzviinu-thumb-346754727"
    },
    {
        "id": 3,
        "name": "Sony PlayStation 5",
        "description": "The Sony PlayStation 5 features an AMD Zen 2-based CPU, AMD RDNA 2-based GPU, and 16GB of GDDR6 memory.",
        "price": 499.99,
        "category": "Electronics",
        "image": "https://www.sony.com/image/44baa604124b770c82401a2dbd78ebaf?fmt=pjpeg&wid=720&bgcolor=F1F5F9&bgc=F1F5F9"
    },
    {
        "id": 4,
        "name": "LG OLED55CXPUA 55-inch 4K OLED TV",
        "description": "The LG OLED55CXPUA 55-inch 4K OLED TV features OLED Display, 4K UHD Resolution, HDR10 Pro, HLG Pro, Dolby Vision IQ, and Dolby Atmos.",
        "price": 1599.99,
        "category": "Electronics",
        "image": "https://www.lg.com/us/images/tvs/md07501804/gallery/desktop-01.jpg"
    },
    {
        "id": 5,
        "name": "Bose QuietComfort 35 II Wireless Headphones",
        "description": "The Bose QuietComfort 35 II Wireless Headphones feature world-class noise cancellation and voice control.",
        "price": 299.00,
        "category": "Electronics",
        "image": "https://assets.bose.com/content/dam/Bose_DAM/Web/consumer_electronics/global/products/headphones/quietcomfort_35_ii_silver/product_silo_images/qc35ii_silver_EC_hero_010719.jpeg"
    },
    {
        "id": 6,
        "name": "Fitbit Versa 3 Smartwatch",
        "description": "The Fitbit Versa 3 Smartwatch features a built-in GPS, Active Zone Minutes, and voice assistant.",
        "price": 229.95,
        "category": "Electronics",
        "image": "https://www.fitbit.com/global/content/dam/fitbit/global/pdp/versa-3/hero/PDP-Versa-3-Carbon-Aluminum-Hero.png"
    },
    {
        "id": 7,
        "name": "KitchenAid Stand Mixer",
        "description": "The KitchenAid Stand Mixer features a 5-quart stainless steel bowl, 10-speed settings, and a variety of attachments.",
        "price": 399.99,
        "category": "Home & Kitchen",
        "image": "https://www.kitchenaid.com/content/dam/global/kitchenaid/countertop-appliances/stand-mixers/hero-kitchenaid-stand-mixers-ksm150ps-bw-1600.png"
    },
    {
        "id": 8,
        "name": "Dyson V11 Absolute Cordless Vacuum",
        "description": "The Dyson V11 Absolute Cordless Vacuum features powerful suction and up to 60 minutes of runtime.",
        "price": 699.99,
        "category": "Home Appliances",
        "image": "https://www.dysoncanada.ca/dam/dyson/images/promotions/desktop-promotions/v11-absolute-blue-desktop-3col-242x254.jpg"
    },
    {
        "id": 9,
        "name": "Ninja Foodi Smart XL Grill",
        "description": "The Ninja Foodi Smart XL Grill features 6-in-1 functionality and 4-quart crisper basket.",
        "price": 279.99,
        "category": "Home & Kitchen",
        "image": "https://www.ninjakitchen.com/medias/Ninja-OP500W-Foodi-Smart-XL-6-in-1-Indoor-Grill-with-4-qt-Air-Fryer-and-Dehydrator-2.png"
    },
    {
        "id": 10,
        "name": "Canon EOS Rebel T8i DSLR Camera",
        "description": "The Canon EOS Rebel T8i DSLR Camera features a 24.1-megapixel sensor and DIGIC 8 image processor.",
        "price": 899.00,
        "category": "Electronics",
        "image": "https://www.canon.com.au/-/media/images/products/cameras/dslr/canon-eos-rebel-t8i/canon-eos-rebel-t8i-hero-product-image.jpg"
    }
]

df = pd.DataFrame(data)

df.to_csv("data.csv", index=False)

print("CSV file created successfully!")
print(df)