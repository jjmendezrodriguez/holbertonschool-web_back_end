import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = Pricing._ValidateAmount(amount);
    this._currency = Pricing._Validatecurrency(currency);
  }

  // Get & set for amount
  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    this._amount = Pricing._ValidateAmount(newAmount);
  }

  // Get & set for currency
  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    this._currency = Pricing._Validatecurrency(newCurrency);
  }

  // For display price
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Convert to price
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Both amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }

  // Validate
  static _validateAmount(amount) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    return amount;
  }

  static _validateCurrency(currency) {
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be an instance of Currency');
    }
    return currency;
  }
}
