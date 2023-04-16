// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RenW2{
    // Global variables
    uint256 count = 0;
    mapping(uint => StockListing) public stock;
    mapping(uint => Listing) public listing;
    mapping(uint => User) public users;
    uint256 _value = 0;
    uint256 time;
    uint256 seed = (block.timestamp + block.difficulty) % 100;
    address public owner;
    uint256 CompanyID = 19201;
    uint256 Global_Amount = 1000;
    uint256 Amount_Stock_Price;
    uint256 individual_pricing;
    uint256 User_Count;
    uint256 Weight;
    uint256 quantity;
    uint256 Environment_Info;

    // Defining the User Attributes
    struct User {
        string UserName;
        uint256 UserID;
        uint256 amount;
        uint256 stocksOwned;
    }

    // Constructor to instantiate the User
    constructor() {
        string memory _UserName = "sai";
        uint256 _UserID = 60090;
        uint256 _amount = 1000;
        uint256 _stocksOwned = 0;
        User_Count = 0;
        users[User_Count] = User(_UserName, _UserID, _amount, _stocksOwned);
    }

    //
    struct StockListing {
        string CompanyName;
        string ProjectName;
        uint256 CompanyID;
        uint256 amount;
        uint256 quantity;
    }


    struct Listing {
        string PersonName;
        uint256 stockID;
        uint256 PersonID;
        uint256 CompanyID;
        uint256 amount;
        uint8 count;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    function getTime() public returns (uint256){
    time = (block.timestamp / 3600 ) % 24;
    return time;
    }

    function getRandomNumber() public returns (uint256) {
        seed = (seed + block.timestamp + block.difficulty) % 100;
        return seed;
    }

    function createListing(string memory _Name, string memory _projectName, uint256 _amount, uint256 _quantity) public {
        stock[count] = StockListing(_Name, _projectName, CompanyID, _amount, _quantity);
        individual_pricing = _amount / _quantity;
        Amount_Stock_Price = _amount;
        quantity = _quantity;
        for(uint8 i = 0; i < _quantity; ++i){
            uint256 randomNum = getRandomNumber();
            listing[i] = Listing(stock[count].CompanyName, randomNum, CompanyID, stock[count].CompanyID, individual_pricing, 0);
        }
        count += 1;
    }

    function buyListing(uint256 _listingIndex) public {
        require(listing[_listingIndex].PersonID != users[User_Count].UserID, "Cannot buy the same stock twice");

        listing[_listingIndex].PersonID = users[User_Count].UserID;
        listing[_listingIndex].PersonName = users[User_Count].UserName;
        listing[_listingIndex].count += 1;

        stock[count-1].amount += individual_pricing;
        stock[count-1].quantity -= stock[count-1].quantity;

        users[User_Count].amount -= individual_pricing;
        users[User_Count].stocksOwned += stock[count-1].quantity;

        getWeight();
        }
    }

    function getWeight() private{
        uint256 hour = getTime();
        if (hour >= 18 || hour <= 6){
            Weight = 1;
        }else if(hour > 6 && hour <= 8){
            Weight = 2;
        }else if(hour > 8 && hour <= 10){
            Weight = 3;
        }else if(hour > 10 && hour <= 12){
            Weight = 5;
        }else if(hour > 12 && hour <= 14){
            Weight = 8;
        }else if(hour > 14 && hour <= 16){
            Weight = 11;
        }else if(hour > 16 && hour <= 18){
            Weight = 3;
        }
        Weight = 1 + hour;
        updatePrices();
    }

    function updatePrices() private {
        uint256 price_stock = listing[0].amount;
        price_stock = price_stock + Weight;
        for(uint8 i = 0; i < quantity; ++i){
            listing[i].amount = price_stock;
        }
    }
}