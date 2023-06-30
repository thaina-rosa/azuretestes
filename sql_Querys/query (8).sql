CREATE TABLE SpecialOfferProduct (
    SpecialOfferID INT,
    ProductID INT,
    rowguid VARCHAR(50),
    ModifiedDate TIMESTAMP,
    PRIMARY KEY (SpecialOfferID, ProductID)
);
