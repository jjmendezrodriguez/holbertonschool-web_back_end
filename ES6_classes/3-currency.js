// 3-currency.js

export default class Currency {
    constructor(code, name) {
      this._code = this._validateString(code, 'Code');
      this._name = this._validateString(name, 'Name');
    }
  
    // Validate that value is a string
    _validateString(value, attributeName) {
      if (typeof value !== 'string') {
        throw new TypeError(`${attributeName} must be a string`);
      }
      return value;
    }
  
    // Getter and Setter for code
    get code() {
      return this._code;
    }
  
    set code(value) {
      this._code = this._validateString(value, 'Code');
    }
  
    // Getter and Setter for name
    get name() {
      return this._name;
    }
  
    set name(value) {
      this._name = this._validateString(value, 'Name');
    }
  
    // Method to display the full currency
    displayFullCurrency() {
      return `${this._name} (${this._code})`;
    }
  }
  