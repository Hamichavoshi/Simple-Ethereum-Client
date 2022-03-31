// SPDX-License-Identifier: GPL-3.0

// Storage.sol

pragma solidity >=0.4.16 <0.9.0;

contract Storage {
    uint storedData;

    event ValueModified(
        uint oldValue,
        uint newValue
    );

    constructor(uint initValue) {
        storedData = initValue;
    }

    function set(uint newValue) public {
        emit ValueModified(storedData, newValue);
        storedData = newValue;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}