from django.db import migrations

def load_initial_data(apps, schema_editor):
    Table = apps.get_model('reservations', 'Table')
    tables_data = [
        ('Berlin Table', 4, 'View of the garden'),
        ('Munich Table', 16, 'View of the street'),
        ('Vienna Table', 23, 'View of the garden'),
        ('Zurich Table', 5, 'View of the plaza'),
        ('Tokyo Table', 18, 'View of the skyline'),
        ('Kyoto Table', 2, 'View of the waterfall'),
        ('Geneva Table', 60, 'View of the mountains'),
        ('Toronto Table', 4, 'View of the lake'),
        ('Paris Table', 5, 'View of the river'),
        ('New York Table', 2, 'View of the park'),
        ('Los Angeles Table', 7, 'View of the cityscape'),
        ('London Table', 2, 'View of the terrace'),
        ('Edinburgh Table', 8, 'View of the forest'),
        ('San Francisco Table', 6, 'View of the bay'),
        ('Florence Table', 4, 'View of the vineyard'),
        ('Lisbon Table', 3, 'View of the ocean'),
        ('Barcelona Table', 5, 'View of the garden'),
        ('Vancouver Table', 4, 'View of the mountains'),
        ('Oslo Table', 6, 'View of the forest'),
        ('Dubai Table', 8, 'View of the skyline')
    ]

    for name, seats, description in tables_data:
        Table.objects.create(number=name, seats=seats, description=description)

class Migration(migrations.Migration):
    dependencies = [
        ('reservations','0005_alter_reservation_guests.py'), 
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
