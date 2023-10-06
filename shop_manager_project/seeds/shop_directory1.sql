DROP TABLE IF EXISTS "public"."items" CASCADE;
DROP SEQUENCE IF EXISTS items_id_seq;
-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS items_id_seq;
-- Table Definition
CREATE TABLE "public"."items" (
    "id" int4 NOT NULL DEFAULT nextval('items_id_seq'::regclass),
    "name" text,
    "unit_price" float8,
    "quantity" int4,
    PRIMARY KEY ("id")
);

DROP TABLE IF EXISTS "public"."items_orders" CASCADE;
-- Table Definition
CREATE TABLE "public"."items_orders" (
    "item_id" int4 NOT NULL,
    "order_id" int4 NOT NULL,
    PRIMARY KEY ("item_id","order_id")
);

DROP TABLE IF EXISTS "public"."orders" CASCADE;
DROP SEQUENCE IF EXISTS orders_id_seq;
-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
-- Table Definition
CREATE TABLE "public"."orders" (
    "id" int4 NOT NULL DEFAULT nextval('orders_id_seq'::regclass),
    "customer_name" text,
    "date_ordered" date,
    PRIMARY KEY ("id")
);

INSERT INTO "public"."items" ("name", "unit_price", "quantity") VALUES
('banana', 0.8, 30),
('apple', 0.9, 20),
('white bread', 1.5, 15),
('orange juice', 1.8, 10),
('apple juice', 1.8, 12),
('wine', 6, 30),
('beer', 3.2, 60);

INSERT INTO "public"."items_orders" ("item_id", "order_id") VALUES
(1, 1),
(1, 3),
(1, 4),
(2, 1),
(2, 2),
(2, 3),
(4, 1),
(5, 2),
(5, 5),
(6, 3),
(6, 5),
(7, 2);

INSERT INTO "public"."orders" ("customer_name", "date_ordered") VALUES
('Kieran', '2023-09-10'),
('James', '2023-09-11'),
('Jack', '2023-09-12'),
('Jane', '2023-09-11'),
('Leo', '2023-09-10');

ALTER TABLE "public"."items_orders" ADD FOREIGN KEY ("order_id") REFERENCES "public"."orders"("id") ON DELETE CASCADE;
ALTER TABLE "public"."items_orders" ADD FOREIGN KEY ("item_id") REFERENCES "public"."items"("id") ON DELETE CASCADE;
