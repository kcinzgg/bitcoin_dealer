from abc import ABCMeta, abstractmethod, abstractproperty
import bitcoin_dealer.settings as settings

class Order:
    """
    This one is not abstract, but just base class for setting 
    exchange["blabla"].order.trades = exchanges["blabla"].get_order(trades)
    """
    trades = None

class ExchangeAbstract:
    __metaclass__ = ABCMeta

    """
    @abstractproperty
    def order(self):
        return 'Should never see this'
    
    @order.setter
    def order(self, order):
        return

    def __init__(self):
        self._order = None
            
    """

    @abstractmethod
    def get_orders(self):
        """
        Retrieves orders for particular exchange.

        This method is used for check_status function in scripts/dealing.py,
        but right now, when only MtGox API version 1 is implemented, returned
        data is not structured. I/you should do it, when implementing support
        for other exchanges.
        """

        return None

    @abstractmethod
    def get_last_price(self, currency):
        """
        Retrieves last price from for particular currency.

        Should return Decimal value of a price.
        """

        return None

    @abstractmethod
    def buy(self, price, amount, currency):
        """ 
        bid == buy

        Should return order ID if order was placed successfully.
        """

        return None

    @abstractmethod
    def sell(self, price, amount, currency):
        """ 
        bid == buy

        Should return order ID if order was placed successfully.
        """

        return None
