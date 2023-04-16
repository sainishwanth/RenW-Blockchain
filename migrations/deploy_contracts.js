const RenW = artifacts.require("Migrations");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
