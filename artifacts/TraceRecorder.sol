// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract TraceRecorder {
    uint256 public value;
    string public message;
    address public lastOperator;

    event ValueChanged(
        address indexed operator,
        uint256 oldValue,
        uint256 newValue,
        string note
    );

    event MessageChanged(
        address indexed operator,
        string oldMessage,
        string newMessage
    );

    constructor(uint256 initValue, string memory initMessage) {
        value = initValue;
        message = initMessage;
        lastOperator = msg.sender;
    }

    function readAll() public view returns (uint256, string memory, address) {
        return (value, message, lastOperator);
    }

    function setValue(uint256 newValue, string memory note) public {
        uint256 oldValue = value;
        value = newValue;
        lastOperator = msg.sender;
        emit ValueChanged(msg.sender, oldValue, newValue, note);
    }

    function setMessage(string memory newMessage) public {
        string memory oldMessage = message;
        message = newMessage;
        lastOperator = msg.sender;
        emit MessageChanged(msg.sender, oldMessage, newMessage);
    }
}
