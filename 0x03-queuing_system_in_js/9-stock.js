import express from 'express';
import { createClient } from 'redis';

const listProducts = [
    {
        itemId: 1,
        itemName: 'Suitcase 250',
        price: 50,
        initialAvailableQuantity: 4
    },
    {
        itemId: 2,
        itemName: 'Suitcase 450',
        price: 100,
        initialAvailableQuantity: 10
    },
    {
        itemId: 3,
        itemName: 'Suitcase 650',
        price: 350,
        initialAvailableQuantity: 2
    },
    {
        itemId: 4,
        itemName: 'Suitcase 1050',
        price: 550,
        initialAvailableQuantity: 5
    },
];

const getItemById = (id) => {
    return listProducts.find(product => product.itemId === id);
};

const app = express();
const client = createClient();
const port = 1245;

const reserveStockById = async (itemId, stock) => {
    await client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
    const stock = await client.get(`item.${itemId}`);
    return stock ? parseInt(stock) : 0;
};

app.get('/list_products', (_, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
    const stock = await getCurrentReservedStockById(req.params.itemId);
    const item = getItemById(Number(req.params.itemId));

    if (!item) {
        res.json({ status: 'Product not found' });
    } else {
        res.json({
            ...item,
            currentQuantity: item.stock - stock,
        });
    }
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const stock = await getCurrentReservedStockById(req.params.itemId);
    const item = getItemById(Number(req.params.itemId));

    if (!item) {
        res.json({ status: 'Product not found' });
    } else {
        if (stock >= item.stock) {
            res.json({ status: 'Not enough stock available', itemId: item.itemId });
        } else {
            await reserveStockById(item.itemId, stock + 1);
            res.json({ status: 'Reservation confirmed', itemId: item.itemId });
        }
    }
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

