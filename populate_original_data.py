
import os
import django
import sys

# Add the project directory to sys.path
# BASE_DIR is online_project/
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_project.settings')
django.setup()

from shop.models import Category, Product

# Category Data from download_real_images.py
category_data = [
    ('Electronics', 'uploads/20251120000226electronics_cat.png', 'Modern electronics and gadgets'),
    ('Fashion', 'uploads/20251120000226fashion_cat.png', 'Latest fashion trends and apparel'),
    ('Wearables', 'uploads/20251120000226wearables_cat.png', 'Smart devices you can wear'),
    ('Photography', 'uploads/20251120000226photography_cat.png', 'Cameras, lenses and photography gear'),
    ('Audio', 'uploads/20251120000226audio_cat.png', 'Headphones, speakers and audio equipment'),
    ('Home & Living', 'uploads/20251120000226home__living_cat.png', 'Furniture and home decor'),
    ('Sports & Outdoors', 'uploads/20251120000226sports__outdoors_cat.png', 'Gear for sports and outdoor activities'),
    ('Books & Stationery', 'uploads/20251120000226books__stationery_cat.png', 'Books, notebooks and office supplies'),
    ('Beauty & Personal Care', 'uploads/20251120000226beauty__personal_care_cat.png', 'Skincare, makeup and personal care'),
    ('Kitchen & Dining', 'uploads/20251120000226kitchen__dining_cat.png', 'Kitchenware and dining essentials'),
    ('Gaming', 'uploads/20251120000755gaming_cat.png', 'Gaming consoles, PCs and accessories'),
    ('Home & Kitchen', 'uploads/20251120095918home__kitchen.jpg', 'Essentials for your home and kitchen')
]

# Product List from download_real_images.py
products_list = [
    ('Wireless Headphones', 'uploads/20251119234028headphones_main.png', 2999, 1999, 'High-quality wireless headphones with noise cancellation'),
    ('Smartphone Pro Max', 'uploads/20251120000226smartphone_pro_max_main.png', 89999, 79999, 'The most powerful smartphone with advanced camera system'),
    ('UltraBook Laptop', 'uploads/20251120000226ultrabook_laptop_main.png', 65000, 54999, 'Slim and powerful laptop for professionals'),
    ('Smart Watch Pro', 'uploads/20251120000226smart_watch_pro_main.png', 15000, 12999, 'Advanced health tracking and smart notifications'),
    ('Professional DSLR Camera', 'uploads/20251120000226professional_dslr_camera_main.png', 45000, 39999, 'Capture stunning photos with this professional DSLR'),
    ('Premium Cotton T-Shirt', 'uploads/20251120000226premium_cotton_t-shirt_main.png', 999, 599, 'Comfortable and stylish 100% cotton t-shirt'),
    ('Athletic Sneakers', 'uploads/20251120000226athletic_sneakers_main.png', 4999, 2999, 'Durable sneakers for all your athletic needs'),
    ('Travel Backpack', 'uploads/20251120000226travel_backpack_main.png', 2500, 1499, 'Spacious and ergonomic backpack for travelers'),
    ('Tablet Pro 12.9', 'uploads/20251120000226tablet_pro_12.9_main.png', 79999, 69999, 'Large display tablet for creative work'),
    ('Fitness Tracker Band', 'uploads/20251120000226fitness_tracker_band_main.png', 2999, 1999, 'Track your daily activity and heart rate'),
    ('Mirrorless Camera Kit', 'uploads/20251120000226mirrorless_camera_kit_main.png', 55000, 49999, 'Compact mirrorless camera with versatile lens'),
    ('Wireless Noise-Canceling Headphones', 'uploads/20251120000226wireless_noise-canceling_headphones_main.png', 5999, 4499, 'Tune out the world with premium noise canceling'),
    ('Bluetooth Speaker', 'uploads/20251120000226bluetooth_speaker_main.png', 3500, 2499, 'Portable bluetooth speaker with rich bass'),
    ('Modern Desk Lamp', 'uploads/20251120000226modern_desk_lamp_main.png', 1500, 999, 'Sleek desk lamp for your workspace'),
    ('Ergonomic Office Chair', 'uploads/20251120000226ergonomic_office_chair_main.png', 12000, 8999, 'Comfortable chair for long working hours'),
    ('Yoga Mat Premium', 'uploads/20251120000226yoga_mat_premium_main.png', 1200, 799, 'Non-slip yoga mat for your fitness routine'),
    ('Basketball Official Size', 'uploads/20251120000226basketball_official_size_main.png', 1500, 999, 'Official size and weight basketball'),
    ('Premium Notebook Set', 'uploads/20251120000226premium_notebook_set_main.png', 800, 499, 'High-quality paper notebooks for writing'),
    ('Luxury Face Cream', 'uploads/20251120000226luxury_face_cream_main.png', 2500, 1999, 'Rejuvenating face cream with natural ingredients'),
    ('High-Speed Blender', 'uploads/20251120000226high-speed_blender_main.png', 4500, 3499, 'Powerful blender for smoothies and more'),
    ('Gaming Laptop RTX 4080', 'uploads/20251120000755gaming_laptop_rtx_4080_main.png', 150000, 139999, 'Ultimate gaming performance with RTX 4080'),
    ('Wireless Gaming Headset', 'uploads/20251120000755wireless_gaming_headset_main.png', 8000, 5999, 'Lag-free wireless audio for gamers'),
    ('Mechanical Gaming Keyboard RGB', 'uploads/20251120000755mechanical_gaming_keyboard_rgb_main.png', 5000, 3499, 'Clicky mechanical keys with customizable RGB'),
    ('Gaming Mouse Pro', 'uploads/20251120000755gaming_mouse_pro_main.png', 4000, 2499, 'High-precision gaming mouse for competitive play'),
    ('Gaming Monitor 27" 144Hz', 'uploads/20251120000755gaming_monitor_27_144hz_main.png', 25000, 19999, 'Smooth 144Hz refresh rate for gaming'),
    ('Gaming Chair Ergonomic', 'uploads/20251120000755gaming_chair_ergonomic_main.png', 18000, 14999, 'Race-style chair for ultimate comfort'),
    ('Gaming Controller Wireless', 'uploads/20251120000755gaming_controller_wireless_main.png', 4500, 3499, 'Wireless controller for PC and console'),
    ('Gaming Mousepad XXL', 'uploads/20251120000755gaming_mousepad_xxl_main.png', 1500, 999, 'Large surface for keyboard and mouse'),
    ('Gaming Webcam 1080p', 'uploads/20251120000755gaming_webcam_1080p_main.png', 5000, 3999, 'Full HD webcam for streaming and calls'),
    ('Gaming Backpack', 'uploads/20251120000755gaming_backpack_main.png', 3500, 2499, 'Protect your gaming gear on the go'),
    ('Wireless Bluetooth Headphones', 'uploads/20251120095919Wireless_Bluetooth_Headphones_main.jpg', 3500, 2499, 'Versatile bluetooth headphones'),
    ('Portable Laptop Stand', 'uploads/20251120095921Portable_Laptop_Stand_main.jpg', 1200, 799, 'Adjustable stand for better ergonomics'),
    ('Designer Leather Jacket', 'uploads/20251120095922Designer_Leather_Jacket_main.jpg', 8000, 5999, 'Premium leather jacket for a stylish look'),
    ('Canvas Sneakers', 'uploads/20251120095925Canvas_Sneakers_main.jpg', 2500, 1499, 'Casual sneakers for everyday wear'),
    ('Stainless Steel Coffee Maker', 'uploads/20251120095926Stainless_Steel_Coffee_Maker_main.jpg', 5000, 3999, 'Brew delicious coffee at home'),
    ('Ceramic Cookware Set', 'uploads/20251120095929Ceramic_Cookware_Set_main.jpg', 7000, 5499, 'Non-stick ceramic pans and pots'),
    ('Camping Tent 4-Person', 'uploads/20251120095931Camping_Tent_4-Person_main.jpg', 10000, 7999, 'Spacious tent for outdoor adventures'),
    ('LED Desk Lamp', 'uploads/20251120095933LED_Desk_Lamp_main.jpg', 1000, 699, 'Energy-efficient LED lamp'),
    ('Denim Blue Jeans', 'uploads/20251120100250Denim_Blue_Jeans_main.jpg', 2500, 1499, 'Classic denim jeans with a perfect fit'),
    ('Casual Cotton T-Shirt', 'uploads/20251120100252Casual_Cotton_T-Shirt_main.jpg', 800, 499, 'Simple cotton t-shirt for daily use'),
    ('Formal Dress Shirt', 'uploads/20251120100255Formal_Dress_Shirt_main.jpg', 2000, 1299, 'Smart formal shirt for office and events'),
    ('Summer Floral Dress', 'uploads/20251120100258Summer_Floral_Dress_main.jpg', 3500, 2499, 'Beautiful floral dress for summer'),
    ('Wool Blazer', 'uploads/20251120100302Wool_Blazer_main.jpg', 6000, 4499, 'Elegant wool blazer for a sharp look'),
    ('Running Sports Shoes', 'uploads/20251120100314Running_Sports_Shoes_main.jpg', 4500, 2999, 'Lightweight shoes for running'),
    ('Aviator Sunglasses', 'uploads/20251120100329Aviator_Sunglasses_main.jpg', 1500, 999, 'Classic aviator style sunglasses'),
    ('Knit Wool Sweater', 'uploads/20251120100333Knit_Wool_Sweater_main.jpg', 2500, 1799, 'Warm knit sweater for cold weather'),
    ('Crossbody Handbag', 'uploads/20251120100336Crossbody_Handbag_main.jpg', 4000, 2499, 'Stylish handbag for daily essentials'),
    ('Ankle Boots Leather', 'uploads/20251120100343Ankle_Boots_Leather_main.jpg', 5500, 3999, 'Durable leather boots with ankle support'),
    ('Chinos Khaki Pants', 'uploads/20251120100348Chinos_Khaki_Pants_main.jpg', 1800, 1199, 'Comfortable khaki pants for casual wear'),
    ('Hoodie Pullover', 'uploads/20251120100350Hoodie_Pullover_main.jpg', 2000, 1499, 'Cozy hoodie for a relaxed look'),
    ('Baseball Cap', 'uploads/20251120100355Baseball_Cap_main.jpg', 800, 499, 'Classic baseball cap for sunny days'),
    ('Maxi Skirt Elegant', 'uploads/20251120100358Maxi_Skirt_Elegant_main.jpg', 2500, 1799, 'Long and flowing skirt for any occasion'),
    ('Polo Shirt Classic', 'uploads/20251120100403Polo_Shirt_Classic_main.jpg', 1200, 799, 'Traditional polo shirt with a smart collar'),
    ('Wireless Gaming Mouse', 'uploads/20251120101034Wireless_Gaming_Mouse_main.jpg', 3500, 2499, 'Fast wireless mouse for gamers'),
    ('Mechanical Keyboard RGB', 'uploads/20251120101044Mechanical_Keyboard_RGB_main.jpg', 4500, 3299, 'Durable mechanical keyboard with RGB'),
    ('USB-C Hub Adapter', 'uploads/20251120101057USB-C_Hub_Adapter_main.jpg', 2000, 1499, 'Expand your connectivity with this hub'),
    ('Portable Power Bank 20000mAh', 'uploads/20251120101106Portable_Power_Bank_20000mAh_main.jpg', 2500, 1799, 'High-capacity power bank for your devices'),
    ('4K Webcam HD', 'uploads/202511201011184K_Webcam_HD_main.jpg', 6000, 4499, 'Crystal clear 4K video for streaming'),
    ('Bluetooth Speaker Portable', 'uploads/20251120101123Bluetooth_Speaker_Portable_main.jpg', 2000, 1299, 'Small yet powerful bluetooth speaker'),
    ('External SSD 1TB', 'uploads/20251120101146External_SSD_1TB_main.jpg', 8000, 6499, 'Fast external storage for your files'),
    ('Wireless Earbuds Pro', 'uploads/20251120101157Wireless_Earbuds_Pro_main.jpg', 5000, 3499, 'True wireless earbuds with great sound'),
    ('USB Microphone Studio', 'uploads/20251120101245USB_Microphone_Studio_main.jpg', 4500, 3299, 'Studio-quality microphone for recording'),
    ('Graphics Drawing Tablet', 'uploads/20251120101303Graphics_Drawing_Tablet_main.jpg', 6000, 4999, 'Precise tablet for digital artists'),
    ('Security Camera WiFi', 'uploads/20251120101327Security_Camera_WiFi_main.jpg', 3500, 2499, 'Monitor your home with this WiFi camera'),
    ('Phone Tripod Mount', 'uploads/20251120101342Phone_Tripod_Mount_main.jpg', 1000, 599, 'Steady mount for your phone photography'),
    ('Blender High Speed', 'uploads/20251120101407Blender_High_Speed_main.jpg', 4000, 2999, 'Blend anything with this high-speed blender'),
    ('Air Fryer Digital', 'uploads/20251120101416Air_Fryer_Digital_main.jpg', 6000, 4499, 'Healthy frying with little to no oil'),
    ('Knife Set Professional', 'uploads/20251120101439Knife_Set_Professional_main.jpg', 5000, 3499, 'Sharp and durable knife set for chefs'),
    ('Vacuum Cleaner Cordless', 'uploads/20251120101457Vacuum_Cleaner_Cordless_main.jpg', 12000, 8999, 'Easy cleaning with this cordless vacuum'),
    ('Rice Cooker Multi-Function', 'uploads/20251120101520Rice_Cooker_Multi-Function_main.jpg', 3500, 2499, 'Perfect rice every time'),
    ('Dish Rack Stainless Steel', 'uploads/20251120101542Dish_Rack_Stainless_Steel_main.jpg', 1500, 999, 'Keep your kitchen organized'),
    ('Toaster Oven Convection', 'uploads/20251120101556Toaster_Oven_Convection_main.jpg', 4500, 3299, 'Versatile oven for baking and toasting'),
    ('Mixing Bowl Set', 'uploads/20251120101616Mixing_Bowl_Set_main.jpg', 1200, 799, 'Versatile bowls for food prep'),
    ('Electric Kettle Glass', 'uploads/20251120101639Electric_Kettle_Glass_main.jpg', 1800, 1299, 'Fast boiling with stylish glass design'),
    ('Food Storage Container Set', 'uploads/20251120101734Food_Storage_Container_Set_main.jpg', 2000, 1499, 'Keep your food fresh longer'),
    ('Pressure Cooker Instant', 'uploads/20251120101759Pressure_Cooker_Instant_main.jpg', 6000, 4499, 'Fast cooking for busy people'),
    ('Trash Can Touchless', 'uploads/20251120101804Trash_Can_Touchless_main.jpg', 2500, 1799, 'Hygienic touchless trash can'),
    ('Cutlery Set 24-Piece', 'uploads/20251120101812Cutlery_Set_24-Piece_main.jpg', 3000, 1999, 'Standard cutlery for your dining table'),
    ('Wine Rack Countertop', 'uploads/20251120101817Wine_Rack_Countertop_main.jpg', 1500, 999, 'Elegant storage for your wine bottles'),
    ('Kitchen Scale Digital', 'uploads/20251120101822Kitchen_Scale_Digital_main.jpg', 1000, 699, 'Precise measurement for cooking'),
    ('Spice Rack Organizer', 'uploads/20251120101840Spice_Rack_Organizer_main.jpg', 1200, 799, 'Keep your spices within reach'),
    ('Can Opener Electric', 'uploads/20251120101853Can_Opener_Electric_main.jpg', 1000, 699, 'Open cans effortlessly'),
    ('Dumbbell Set Adjustable', 'uploads/20251120101901Dumbbell_Set_Adjustable_main.jpg', 5000, 3999, 'Adjustable weights for home workout'),
    ('Resistance Bands Set', 'uploads/20251120101911Resistance_Bands_Set_main.jpg', 1500, 999, 'Versatile bands for strength training'),
    ('Treadmill Folding', 'uploads/20251120101922Treadmill_Folding_main.jpg', 35000, 24999, 'Compact treadmill for home cardio'),
    ('Bicycle Mountain Bike', 'uploads/20251120101933Bicycle_Mountain_Bike_main.jpg', 20000, 14999, 'Durable mountain bike for trails'),
    ('Water Bottle Insulated', 'uploads/20251120101936Water_Bottle_Insulated_main.jpg', 1000, 699, 'Keep your drinks cold or hot'),
    ('Jump Rope Speed', 'uploads/20251120101939Jump_Rope_Speed_main.jpg', 600, 399, 'Fast rope for better cardio'),
    ('Basketball Indoor/Outdoor', 'uploads/20251120102201Basketball Indoor/Outdoor_main.jpg', 1800, 1299, 'Durable basketball for any court'),
    ('Tennis Racket Carbon', 'uploads/20251120102204Tennis_Racket_Carbon_main.jpg', 4500, 3499, 'Lightweight carbon fiber racket'),
    ('Skateboard Complete', 'uploads/20251120102220Skateboard_Complete_main.jpg', 3500, 2499, 'Ready to ride skateboard'),
    ('Swimming Goggles Pro', 'uploads/20251120102244Swimming_Goggles_Pro_main.jpg', 1200, 799, 'Anti-fog goggles for swimmers'),
    ('Badminton Racket Set', 'uploads/20251120102257Badminton_Racket_Set_main.jpg', 2000, 1499, 'Set of two rackets and shuttlecocks'),
    ('Foam Roller Massage', 'uploads/20251120102304Foam_Roller_Massage_main.jpg', 1500, 999, 'Recover faster with foam rolling'),
    ('Gym Bag Duffle', 'uploads/20251120102309Gym_Bag_Duffle_main.jpg', 2000, 1299, 'Spacious bag for all your gym gear')
]

# Helper to assign category
def get_category_for_product(product_name):
    name = product_name.lower()
    if any(k in name for k in ['laptop', 'monitor', 'phone', 'tablet', 'camera', 'dslr', 'webcam', 'ssd', 'hub', 'power bank', 'tripod', 'microphone']):
        return 'Electronics'
    if any(k in name for k in ['t-shirt', 'shirt', 'dress', 'jeans', 'blazer', 'jacket', 'sweater', 'handbag', 'boots', 'pants', 'hoodie', 'cap', 'skirt', 'polo', 'suit', 'apparel', 'silk', 'kurta']):
        return 'Fashion'
    if any(k in name for k in ['watch', 'band', 'earbuds', 'wearable']):
        return 'Wearables'
    if any(k in name for k in ['headphone', 'speaker', 'audio', 'earphone']):
        return 'Audio'
    if any(k in name for k in ['gaming', 'controller', 'mousepad', 'keyboard', 'mouse']):
        return 'Gaming'
    if any(k in name for k in ['blender', 'fryer', 'knife', 'vacuum', 'rice cooker', 'dish rack', 'oven', 'bowl', 'kettle', 'container', 'trash can', 'cutlery', 'wine rack', 'scale', 'spice rack', 'can opener', 'cookware', 'coffee maker']):
        return 'Home & Kitchen'
    if any(k in name for k in ['basketball', 'tennis', 'bicycle', 'dummbell', 'treadmill', 'jump rope', 'skateboard', 'goggles', 'badminton', 'roller', 'gym bag', 'mountain bike', 'sports shoes', 'sneakers', 'yoga mat', 'fitness']):
        return 'Sports & Outdoors'
    if any(k in name for k in ['cream', 'beauty', 'skincare', 'makeup']):
        return 'Beauty & Personal Care'
    if any(k in name for k in ['notebook', 'stationery', 'book', 'pen']):
        return 'Books & Stationery'
    if any(k in name for k in ['lamp', 'chair', 'desk', 'decor', 'furniture']):
        return 'Home & Living'
    return 'Home & Kitchen' # Default

def populate():
    print("Populating Categories...")
    cat_map = {}
    for name, img, desc in category_data:
        cat, created = Category.objects.get_or_create(
            name=name,
            defaults={'images': img, 'description': desc, 'status': False}
        )
        if not created:
            cat.images = img
            cat.description = desc
            cat.save()
        cat_map[name] = cat
        print(f"  Category: {name} ({'Created' if created else 'Updated'})")

    print("\nPopulating Products...")
    for name, img, o_price, s_price, desc in products_list:
        cat_name = get_category_for_product(name)
        cat = cat_map.get(cat_name)
        if not cat:
            print(f"  Warning: Category {cat_name} not found for product {name}")
            continue
            
        prod, created = Product.objects.get_or_create(
            name=name,
            category=cat,
            defaults={
                'vendor': 'ShopKart',
                'quantity': 100,
                'original_price': o_price,
                'selling_price': s_price,
                'product_images': img,
                'description': desc,
                'status': False,
                'trending': any(k in name.lower() for k in ['pro', 'max', 'gaming', 'premium', 'ultra'])
            }
        )
        if not created:
            prod.product_images = img
            prod.original_price = o_price
            prod.selling_price = s_price
            prod.description = desc
            prod.trending = any(k in name.lower() for k in ['pro', 'max', 'gaming', 'premium', 'ultra'])
            prod.save()
        print(f"  Product: {name} ({'Created' if created else 'Updated'})")

if __name__ == '__main__':
    populate()
    print("\nSync completed successfully!")
