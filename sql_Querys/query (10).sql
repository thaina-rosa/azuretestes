CREATE TABLE SalesOrder (
    SalesOrderID INT,
    SalesOrderDetailID INT,
    CarrierTrackingNumber VARCHAR(50),
    OrderQty INT,
    ProductID INT,
    SpecialOfferID INT,
    UnitPrice FLOAT,
    UnitPriceDiscount FLOAT,
    LineTotal FLOAT,
    rowguid VARCHAR(50),
    ModifiedDate TIMESTAMP,
    PRIMARY KEY (SalesOrderID, SalesOrderDetailID)
);
