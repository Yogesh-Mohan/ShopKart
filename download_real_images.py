
import os
import urllib.request
import time
import random

# Base static directory
static_dir = os.path.join(os.getcwd(), 'static')
uploads_dir = os.path.join(static_dir, 'uploads')

if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

# Helper function to download image
def download_image(url, filename, retries=3):
    # Ensure URL has high quality parameters if it's Unsplash
    if 'unsplash.com' in url and '?' not in url:
        url += '?auto=format&fit=crop&w=1080&q=80'
    elif 'unsplash.com' in url and '?' in url:
        url += '&auto=format&fit=crop&w=1080&q=80'

    full_path = os.path.join(static_dir, filename)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    for attempt in range(retries):
        try:
            print(f"Downloading {filename}...")
            # Use a realistic user agent
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')]
            urllib.request.install_opener(opener)
            
            urllib.request.urlretrieve(url, full_path)
            # Verify file size
            if os.path.getsize(full_path) < 1000:
                print(f"Warning: Downloaded file {filename} is too small, retrying...")
                continue
                
            print(f"Success: {full_path} ({os.path.getsize(full_path)} bytes)")
            return True
        except Exception as e:
            print(f"Error downloading {filename} (Attempt {attempt+1}): {e}")
            time.sleep(1)
    return False

# Category Images (Unsplash URLs)
category_data = [
    ('Fashion', 'uploads/20251120000226fashion_cat.png', 'https://images.unsplash.com/photo-1483985988355-763728e1935b'),
    ('Wearables', 'uploads/20251120000226wearables_cat.png', 'https://images.unsplash.com/photo-1579586337278-3befd40fd17a'),
    ('Photography', 'uploads/20251120000226photography_cat.png', 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32'),
    ('Audio', 'uploads/20251120000226audio_cat.png', 'https://images.unsplash.com/photo-1546435770-a3e426bf472b'),
    ('Home & Living', 'uploads/20251120000226home__living_cat.png', 'https://images.unsplash.com/photo-1484101403633-562f891dc89a'),
    ('Sports & Outdoors', 'uploads/20251120000226sports__outdoors_cat.png', 'https://images.unsplash.com/photo-1517649763962-0c623066013b'),
    ('Books & Stationery', 'uploads/20251120000226books__stationery_cat.png', 'https://images.unsplash.com/photo-1524985069026-dd778a71c7b4'),
    ('Beauty & Personal Care', 'uploads/20251120000226beauty__personal_care_cat.png', 'https://images.unsplash.com/photo-1596462502278-27bfdd403cc2'),
    ('Kitchen & Dining', 'uploads/20251120000226kitchen__dining_cat.png', 'https://images.unsplash.com/photo-1556910103-1c02745a30bf'),
    ('Gaming', 'uploads/20251120000755gaming_cat.png', 'https://images.unsplash.com/photo-1542751371-adc38448a05e'),
    ('Home & Kitchen', 'uploads/20251120095918home__kitchen.jpg', 'https://images.unsplash.com/photo-1556911220-e15b29be8c8f')
]

# Product Images (Unsplash URLs - General Matches)
# Using generic high-quality images for product categories
product_mapping = {
    'headphone': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e',
    'phone': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9',
    'laptop': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853',
    'watch': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30',
    'camera': 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32',
    't-shirt': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab',
    'shirt': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c',
    'sneaker': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff',
    'shoe': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff',
    'backpack': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62',
    'tablet': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0',
    'band': 'https://images.unsplash.com/photo-1579586337278-3befd40fd17a',
    'speaker': 'https://images.unsplash.com/photo-1545459720-aacaf5090834',
    'lamp': 'https://images.unsplash.com/photo-1507473888900-52a1068718ed',
    'chair': 'https://images.unsplash.com/photo-1592078615290-033ee584e267',
    'mat': 'https://images.unsplash.com/photo-1592432678016-e910b452f9a9',
    'basketball': 'https://images.unsplash.com/photo-1518063319789-7217e6706b04',
    'notebook': 'https://images.unsplash.com/photo-1544816155-12df9643f363',
    'cream': 'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881',
    'jacket': 'https://images.unsplash.com/photo-1551028919-ac7f21422ace',
    'coffee': 'https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6',
    'cookware': 'https://images.unsplash.com/photo-1584992236310-6edddc08acff',
    'tent': 'https://images.unsplash.com/photo-1504280506541-aca063246d74',
    'jeans': 'https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a',
    'dress': 'https://images.unsplash.com/photo-1495385794356-15371f348c31',
    'blazer': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf',
    'belt': 'https://images.unsplash.com/photo-1624222247344-550fb60583dc',
    'sunglasses': 'https://images.unsplash.com/photo-1511499767150-a48a237f0083',
    'sweater': 'https://images.unsplash.com/photo-1576566588028-4147f3842f27',
    'handbag': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3',
    'scarf': 'https://images.unsplash.com/photo-1520903920243-00d872a2d1c9',
    'monitor': 'https://images.unsplash.com/photo-1551645120-d70bfe84c826',
    'mouse': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46',
    'keyboard': 'https://images.unsplash.com/photo-1595225476474-87563907a212',
    'hub': 'https://images.unsplash.com/photo-1625805866449-3589fe3f71a3',
    'power bank': 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5',
    'webcam': 'https://images.unsplash.com/photo-1601469550757-41071413ac99',
    'ssd': 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b',
    'earbuds': 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df',
    'tripod': 'https://images.unsplash.com/photo-1527011046414-4781f1f94f8c',
    'blender': 'https://images.unsplash.com/photo-1595981267035-7b04ca84a82d',
    'fryer': 'https://images.unsplash.com/photo-1584992236310-6edddc08acff', # Generic kitchen
    'knife': 'https://images.unsplash.com/photo-1593642532744-d377ab507dc8',
    'vacuum': 'https://images.unsplash.com/photo-1558317374-a354d5f2946f',
    'rice': 'https://images.unsplash.com/photo-1516685018646-549198525c1b',
    'bowl': 'https://images.unsplash.com/photo-1567119253818-8798544b6ac7',
    'kettle': 'https://images.unsplash.com/photo-1556912173-3db996e7c3ac',
    'container': 'https://images.unsplash.com/photo-1584992236310-6edddc08acff',
    'trash': 'https://images.unsplash.com/photo-1530508577583-4ee2636eb01c',
    'cutlery': 'https://images.unsplash.com/photo-1584992236310-6edddc08acff',
    'wine': 'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3',
    'scale': 'https://images.unsplash.com/photo-1599666750958-45ac792f58be',
    'spice': 'https://images.unsplash.com/photo-1596040033229-a9821ebd058d',
    'dumbbell': 'https://images.unsplash.com/photo-1583454110551-21f2fa2afe61',
    'treadmill': 'https://images.unsplash.com/photo-1571902943202-507ec2618e8f',
    'bicycle': 'https://images.unsplash.com/photo-1485965120184-e224f7a1aae4',
    'bottle': 'https://images.unsplash.com/photo-1602143407151-01114192003f',
    'rope': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b',
    'soccer': 'https://images.unsplash.com/photo-1579952363873-27f3bade9f55',
    'tennis': 'https://images.unsplash.com/photo-1628131347076-2e9b8970e782', # Racket fallback
    'skateboard': 'https://images.unsplash.com/photo-1520045864985-83c7ae4b8347',
    'fishing': 'https://images.unsplash.com/photo-1544365558-35aa4afcf11f',
    'goggles': 'https://images.unsplash.com/photo-1576421035048-c30c8227b40c',
    'badminton': 'https://images.unsplash.com/photo-1626224583764-84786c713608',
    'boxing': 'https://images.unsplash.com/photo-1549719386-74dfcbf7dbed',
    'roller': 'https://images.unsplash.com/photo-1600881333168-2ef49b341f30',
    'gym bag': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62',
    'boots': 'https://images.unsplash.com/photo-1608256246200-53e635b5b65f',
    'pants': 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246',
    'hoodie': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7',
    'cap': 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b',
    'skirt': 'https://images.unsplash.com/photo-1583496661160-fb5889a0539d',
    'polo': 'https://images.unsplash.com/photo-1581655353564-df123a1eb820',
    'jeans': 'https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a',
    'kettle': 'https://images.unsplash.com/photo-1594385208974-2e75f9d86347',
    'vacuum': 'https://images.unsplash.com/photo-1558317374-a354d5f2946f'
}

# Explicit Product List (from database dump)
products_list = [
    ('Wireless Headphones', 'uploads/20251119234028headphones_main.png'),
    ('Smartphone Pro Max', 'uploads/20251120000226smartphone_pro_max_main.png'),
    ('UltraBook Laptop', 'uploads/20251120000226ultrabook_laptop_main.png'),
    ('Smart Watch Pro', 'uploads/20251120000226smart_watch_pro_main.png'),
    ('Professional DSLR Camera', 'uploads/20251120000226professional_dslr_camera_main.png'),
    ('Premium Cotton T-Shirt', 'uploads/20251120000226premium_cotton_t-shirt_main.png'),
    ('Athletic Sneakers', 'uploads/20251120000226athletic_sneakers_main.png'),
    ('Travel Backpack', 'uploads/20251120000226travel_backpack_main.png'),
    ('Tablet Pro 12.9', 'uploads/20251120000226tablet_pro_12.9_main.png'),
    ('Fitness Tracker Band', 'uploads/20251120000226fitness_tracker_band_main.png'),
    ('Mirrorless Camera Kit', 'uploads/20251120000226mirrorless_camera_kit_main.png'),
    ('Wireless Noise-Canceling Headphones', 'uploads/20251120000226wireless_noise-canceling_headphones_main.png'),
    ('Bluetooth Speaker', 'uploads/20251120000226bluetooth_speaker_main.png'),
    ('Modern Desk Lamp', 'uploads/20251120000226modern_desk_lamp_main.png'),
    ('Ergonomic Office Chair', 'uploads/20251120000226ergonomic_office_chair_main.png'),
    ('Yoga Mat Premium', 'uploads/20251120000226yoga_mat_premium_main.png'),
    ('Basketball Official Size', 'uploads/20251120000226basketball_official_size_main.png'),
    ('Premium Notebook Set', 'uploads/20251120000226premium_notebook_set_main.png'),
    ('Luxury Face Cream', 'uploads/20251120000226luxury_face_cream_main.png'),
    ('High-Speed Blender', 'uploads/20251120000226high-speed_blender_main.png'),
    ('Gaming Laptop RTX 4080', 'uploads/20251120000755gaming_laptop_rtx_4080_main.png'),
    ('Wireless Gaming Headset', 'uploads/20251120000755wireless_gaming_headset_main.png'),
    ('Mechanical Gaming Keyboard RGB', 'uploads/20251120000755mechanical_gaming_keyboard_rgb_main.png'),
    ('Gaming Mouse Pro', 'uploads/20251120000755gaming_mouse_pro_main.png'),
    ('Gaming Monitor 27" 144Hz', 'uploads/20251120000755gaming_monitor_27_144hz_main.png'),
    ('Gaming Chair Ergonomic', 'uploads/20251120000755gaming_chair_ergonomic_main.png'),
    ('Gaming Controller Wireless', 'uploads/20251120000755gaming_controller_wireless_main.png'),
    ('Gaming Mousepad XXL', 'uploads/20251120000755gaming_mousepad_xxl_main.png'),
    ('Gaming Webcam 1080p', 'uploads/20251120000755gaming_webcam_1080p_main.png'),
    ('Gaming Backpack', 'uploads/20251120000755gaming_backpack_main.png'),
    ('Wireless Bluetooth Headphones', 'uploads/20251120095919Wireless_Bluetooth_Headphones_main.jpg'),
    ('Portable Laptop Stand', 'uploads/20251120095921Portable_Laptop_Stand_main.jpg'),
    ('Designer Leather Jacket', 'uploads/20251120095922Designer_Leather_Jacket_main.jpg'),
    ('Canvas Sneakers', 'uploads/20251120095925Canvas_Sneakers_main.jpg'),
    ('Stainless Steel Coffee Maker', 'uploads/20251120095926Stainless_Steel_Coffee_Maker_main.jpg'),
    ('Ceramic Cookware Set', 'uploads/20251120095929Ceramic_Cookware_Set_main.jpg'),
    ('Camping Tent 4-Person', 'uploads/20251120095931Camping_Tent_4-Person_main.jpg'),
    ('LED Desk Lamp', 'uploads/20251120095933LED_Desk_Lamp_main.jpg'),
    ('Denim Blue Jeans', 'uploads/20251120100250Denim_Blue_Jeans_main.jpg'),
    ('Casual Cotton T-Shirt', 'uploads/20251120100252Casual_Cotton_T-Shirt_main.jpg'),
    ('Formal Dress Shirt', 'uploads/20251120100255Formal_Dress_Shirt_main.jpg'),
    ('Summer Floral Dress', 'uploads/20251120100258Summer_Floral_Dress_main.jpg'),
    ('Wool Blazer', 'uploads/20251120100302Wool_Blazer_main.jpg'),
    ('Running Sports Shoes', 'uploads/20251120100314Running_Sports_Shoes_main.jpg'),
    ('Aviator Sunglasses', 'uploads/20251120100329Aviator_Sunglasses_main.jpg'),
    ('Knit Wool Sweater', 'uploads/20251120100333Knit_Wool_Sweater_main.jpg'),
    ('Crossbody Handbag', 'uploads/20251120100336Crossbody_Handbag_main.jpg'),
    ('Ankle Boots Leather', 'uploads/20251120100343Ankle_Boots_Leather_main.jpg'),
    ('Chinos Khaki Pants', 'uploads/20251120100348Chinos_Khaki_Pants_main.jpg'),
    ('Hoodie Pullover', 'uploads/20251120100350Hoodie_Pullover_main.jpg'),
    ('Baseball Cap', 'uploads/20251120100355Baseball_Cap_main.jpg'),
    ('Maxi Skirt Elegant', 'uploads/20251120100358Maxi_Skirt_Elegant_main.jpg'),
    ('Polo Shirt Classic', 'uploads/20251120100403Polo_Shirt_Classic_main.jpg'),
    ('Wireless Gaming Mouse', 'uploads/20251120101034Wireless_Gaming_Mouse_main.jpg'),
    ('Mechanical Keyboard RGB', 'uploads/20251120101044Mechanical_Keyboard_RGB_main.jpg'),
    ('USB-C Hub Adapter', 'uploads/20251120101057USB-C_Hub_Adapter_main.jpg'),
    ('Portable Power Bank 20000mAh', 'uploads/20251120101106Portable_Power_Bank_20000mAh_main.jpg'),
    ('4K Webcam HD', 'uploads/202511201011184K_Webcam_HD_main.jpg'),
    ('Bluetooth Speaker Portable', 'uploads/20251120101123Bluetooth_Speaker_Portable_main.jpg'),
    ('External SSD 1TB', 'uploads/20251120101146External_SSD_1TB_main.jpg'),
    ('Wireless Earbuds Pro', 'uploads/20251120101157Wireless_Earbuds_Pro_main.jpg'),
    ('USB Microphone Studio', 'uploads/20251120101245USB_Microphone_Studio_main.jpg'),
    ('Graphics Drawing Tablet', 'uploads/20251120101303Graphics_Drawing_Tablet_main.jpg'),
    ('Security Camera WiFi', 'uploads/20251120101327Security_Camera_WiFi_main.jpg'),
    ('Phone Tripod Mount', 'uploads/20251120101342Phone_Tripod_Mount_main.jpg'),
    ('Blender High Speed', 'uploads/20251120101407Blender_High_Speed_main.jpg'),
    ('Air Fryer Digital', 'uploads/20251120101416Air_Fryer_Digital_main.jpg'),
    ('Knife Set Professional', 'uploads/20251120101439Knife_Set_Professional_main.jpg'),
    ('Vacuum Cleaner Cordless', 'uploads/20251120101457Vacuum_Cleaner_Cordless_main.jpg'),
    ('Rice Cooker Multi-Function', 'uploads/20251120101520Rice_Cooker_Multi-Function_main.jpg'),
    ('Dish Rack Stainless Steel', 'uploads/20251120101542Dish_Rack_Stainless_Steel_main.jpg'),
    ('Toaster Oven Convection', 'uploads/20251120101556Toaster_Oven_Convection_main.jpg'),
    ('Mixing Bowl Set', 'uploads/20251120101616Mixing_Bowl_Set_main.jpg'),
    ('Electric Kettle Glass', 'uploads/20251120101639Electric_Kettle_Glass_main.jpg'),
    ('Food Storage Container Set', 'uploads/20251120101734Food_Storage_Container_Set_main.jpg'),
    ('Pressure Cooker Instant', 'uploads/20251120101759Pressure_Cooker_Instant_main.jpg'),
    ('Trash Can Touchless', 'uploads/20251120101804Trash_Can_Touchless_main.jpg'),
    ('Cutlery Set 24-Piece', 'uploads/20251120101812Cutlery_Set_24-Piece_main.jpg'),
    ('Wine Rack Countertop', 'uploads/20251120101817Wine_Rack_Countertop_main.jpg'),
    ('Kitchen Scale Digital', 'uploads/20251120101822Kitchen_Scale_Digital_main.jpg'),
    ('Spice Rack Organizer', 'uploads/20251120101840Spice_Rack_Organizer_main.jpg'),
    ('Can Opener Electric', 'uploads/20251120101853Can_Opener_Electric_main.jpg'),
    ('Dumbbell Set Adjustable', 'uploads/20251120101901Dumbbell_Set_Adjustable_main.jpg'),
    ('Resistance Bands Set', 'uploads/20251120101911Resistance_Bands_Set_main.jpg'),
    ('Treadmill Folding', 'uploads/20251120101922Treadmill_Folding_main.jpg'),
    ('Bicycle Mountain Bike', 'uploads/20251120101933Bicycle_Mountain_Bike_main.jpg'),
    ('Water Bottle Insulated', 'uploads/20251120101936Water_Bottle_Insulated_main.jpg'),
    ('Jump Rope Speed', 'uploads/20251120101939Jump_Rope_Speed_main.jpg'),
    ('Basketball Indoor/Outdoor', 'uploads/20251120102201Basketball Indoor/Outdoor_main.jpg'),
    ('Tennis Racket Carbon', 'uploads/20251120102204Tennis_Racket_Carbon_main.jpg'),
    ('Skateboard Complete', 'uploads/20251120102220Skateboard_Complete_main.jpg'),
    ('Swimming Goggles Pro', 'uploads/20251120102244Swimming_Goggles_Pro_main.jpg'),
    ('Badminton Racket Set', 'uploads/20251120102257Badminton_Racket_Set_main.jpg'),
    ('Foam Roller Massage', 'uploads/20251120102304Foam_Roller_Massage_main.jpg'),
    ('Gym Bag Duffle', 'uploads/20251120102309Gym_Bag_Duffle_main.jpg')
]

# Process Categories
print("Processing Categories...")
for name, filename, url in category_data:
    if filename:
        download_image(url, filename)

# Process Products
print("\nProcessing Products...")
for name, filename in products_list:
    if not filename:
        continue
        
    # Find matching keyword
    found = False
    name_lower = name.lower()
    for key, url in product_mapping.items():
        if key in name_lower:
            download_image(url, filename)
            found = True
            break
    
    if not found:
        # Fallback to random tech/general from Unsplash if no keyword match
        print(f"No specific match for {name}, using fallback.")
        # Use a more generic fashion/product fallback instead of just the polaroid
        fallback_urls = [
            'https://images.unsplash.com/photo-1523275335684-37898b6baf30', # Watch
            'https://images.unsplash.com/photo-1505740420928-5e560c06d30e', # Headphone
            'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f' # Polaroid
        ]
        download_image(random.choice(fallback_urls), filename)
        
print("\nAll download tasks completed.")
