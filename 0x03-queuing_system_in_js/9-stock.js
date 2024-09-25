import express from "express";
import redis from "redis";
import { promisify } from "util";

const app = express();
const port = 1245;

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);

const listProducts = [
	{
		itemId: 1,
		itemName: "Suitcase 250",
		price: 50,
		initialAvailableQuantity: 4,
	},
	{
		itemId: 2,
		itemName: "Suitcase 450",
		price: 100,
		initialAvailableQuantity: 10,
	},
	{
		itemId: 3,
		itemName: "Suitcase 650",
		price: 350,
		initialAvailableQuantity: 2,
	},
	{
		itemId: 4,
		itemName: "Suitcase 1050",
		price: 550,
		initialAvailableQuantity: 5,
	},
];

function getItemById(id) {
	return listProducts.find((product) => product.itemId === parseInt(id));
}

function reserveStockById(itemId, stock) {
	client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
	const stock = await getAsync(`item.${itemId}`);
	return stock !== null ? parseInt(stock) : null;
}

app.get("/list_products", (req, res) => {
	res.json(listProducts);
});

app.get("/list_products/:itemId", async (req, res) => {
	const itemId = req.params.itemId;
	const product = getItemById(itemId);

	if (!product) {
		return res.json({ status: "Product not found" });
	}

	const currentStock = await getCurrentReservedStockById(itemId);
	const currentQuantity =
		currentStock !== null
			? product.initialAvailableQuantity - currentStock
			: product.initialAvailableQuantity;
	res.json({
		itemId: product.itemId,
		itemName: product.itemName,
		price: product.price,
		initialAvailableQuantity: product.initialAvailableQuantity,
		currentQuantity,
	});
});

app.get("/reserve_product/:itemId", async (req, res) => {
	const itemId = req.params.itemId;
	const product = getItemById(itemId);

	if (!product) {
		return res.json({ status: "Product not found" });
	}

	const currentStock = await getCurrentReservedStockById(itemId);
	const availableStock =
		currentStock !== null
			? product.initialAvailableQuantity - currentStock
			: product.initialAvailableQuantity;
	if (availableStock <= 0) {
		return res.json({
			status: "Not enough stock available",
			itemId: product.itemId,
		});
	}
	reserveStockById(itemId, (currentStock || 0) + 1);
	res.json({ status: "Reservation confirmed", itemId: product.itemId });
});

app.listen(port, () => {
	console.log(`Server running on port ${port}`);
});
