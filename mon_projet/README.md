# Django E-commerce Project with Cart and Notifications

This Django project has been enhanced with cart and notification functionality using Django REST Framework APIs that are consumed by the frontend webpage.

## Features Added

### 1. Cart Functionality
- **Add to Cart**: Products can be added to cart with quantity management
- **Update Quantity**: Cart items can have their quantities updated
- **Remove Items**: Individual items can be removed from cart
- **Clear Cart**: All items can be cleared at once
- **Stock Management**: Prevents adding more items than available stock
- **Session-based**: Works for both authenticated and anonymous users
- **Real-time Updates**: Cart badge and sidebar update immediately

### 2. Notification System
- **Notification Types**: Order, Product, Cart, and General notifications
- **Real-time Display**: Notifications appear in a dropdown menu
- **Mark as Read**: Individual or bulk mark as read functionality
- **Auto-refresh**: Notifications refresh every 30 seconds
- **Session-based**: Works for both authenticated and anonymous users

### 3. Dynamic Product Loading
- **API-driven**: Products are loaded dynamically from the backend
- **Real-time Stock**: Shows current stock levels
- **Sale Badges**: Products under $30 show sale badges
- **Responsive Design**: Cards adapt to different screen sizes

## Project Structure

### New Apps Created
```
mon_projet/
├── cart/                    # Cart functionality
│   ├── models.py           # Cart and CartItem models
│   ├── views.py            # Cart API views
│   ├── serializers.py      # Cart API serializers
│   ├── urls.py             # Cart API endpoints
│   └── admin.py            # Admin interface
├── notifications/           # Notification functionality
│   ├── models.py           # Notification model
│   ├── views.py            # Notification API views
│   ├── serializers.py      # Notification API serializers
│   ├── urls.py             # Notification API endpoints
│   └── admin.py            # Admin interface
```

## API Endpoints

### Cart APIs
- `GET /api/cart/` - Get current cart
- `POST /api/cart/add/` - Add product to cart
- `PUT /api/cart/item/<id>/update/` - Update cart item quantity
- `DELETE /api/cart/item/<id>/remove/` - Remove item from cart
- `DELETE /api/cart/clear/` - Clear entire cart

### Notification APIs
- `GET /api/notifications/` - Get all notifications
- `GET /api/notifications/unread/` - Get unread notifications with count
- `PUT /api/notifications/<id>/read/` - Mark notification as read
- `PUT /api/notifications/mark-all-read/` - Mark all notifications as read
- `POST /api/notifications/create/` - Create new notification
- `DELETE /api/notifications/<id>/delete/` - Delete notification

### Product APIs
- `GET /products/api/products/` - Get all products

## Frontend Features

### Cart Sidebar (Offcanvas)
- **Slide-out Design**: Cart opens from the right side
- **Item Management**: Add/remove quantities with +/- buttons
- **Price Calculation**: Shows individual and total prices
- **Stock Validation**: Prevents exceeding available stock
- **Clear All**: Option to clear entire cart

### Notification Dropdown
- **Badge Indicator**: Shows unread count on bell icon
- **Categorized**: Different colors for different notification types
- **Mark Read**: Individual and bulk read options
- **Auto-refresh**: Updates every 30 seconds

### Dynamic Product Grid
- **Responsive Layout**: 2-4 columns based on screen size
- **Stock Display**: Shows available stock count
- **Sale Indicators**: Visual badges for discounted items
- **Interactive Buttons**: Add to cart with stock validation

## Database Models

### Cart Model
```python
class Cart(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    session_key = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### CartItem Model
```python
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items')
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Notification Model
```python
class Notification(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    session_key = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=20)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

## Technologies Used

- **Backend**: Django 5.2.4, Django REST Framework 3.16.0
- **Frontend**: Bootstrap 5.2.3, Vanilla JavaScript
- **Database**: SQLite (default)
- **Icons**: Bootstrap Icons
- **CSRF Protection**: Django's built-in CSRF middleware

## Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install django djangorestframework pillow
   ```

2. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Sample Data** (already included):
   ```bash
   python manage.py shell -c "from products.models import Product; from notifications.models import Notification; ..."
   ```

4. **Start Server**:
   ```bash
   python manage.py runserver
   ```

## Usage

### Adding Products to Cart
1. Navigate to the homepage
2. Click "Add to cart" on any product
3. Cart badge updates with item count
4. Click cart button to view/manage items

### Managing Notifications
1. Notifications appear automatically
2. Click bell icon to view notifications
3. Use "Mark as read" for individual notifications
4. Use "Mark all as read" for bulk operations

### Admin Interface
- Access `/admin/` for backend management
- Manage products, carts, and notifications
- View detailed analytics and user data

## API Testing

Test the APIs using curl or any API client:

```bash
# Get products
curl -X GET http://localhost:8000/products/api/products/

# Get cart
curl -X GET http://localhost:8000/api/cart/

# Add to cart
curl -X POST http://localhost:8000/api/cart/add/ \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "quantity": 2}'

# Get notifications
curl -X GET http://localhost:8000/api/notifications/unread/
```

## Security Features

- **CSRF Protection**: All API calls include CSRF tokens
- **Session Management**: Cart and notifications tied to sessions
- **Input Validation**: All inputs validated through serializers
- **Stock Validation**: Prevents overselling products

## Browser Compatibility

- **Modern Browsers**: Chrome, Firefox, Safari, Edge
- **Bootstrap 5**: Responsive design works on all screen sizes
- **JavaScript ES6+**: Uses modern JavaScript features

This implementation provides a complete e-commerce experience with cart management and notification systems, all integrated seamlessly with the existing Django project structure.