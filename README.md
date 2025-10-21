Implementation notes / OOP features used

Abstraction & Interfaces: AccountBase (an abstract base class) defines contract for account operations.

Inheritance: SavingsAccount, CurrentAccount, FixedDepositAccount inherit AccountBase.

Polymorphism: withdraw()/deposit() implementations differ per subclass where needed.

Encapsulation: Private fields with getters/setters and @property used for controlled access.

Composition/Aggregation: Customer owns multiple Account objects; Bank aggregates Customers.

Class/Static methods: AccountBase.generate_account_number() is a classmethod.

Operator overloading: Transaction.__add__ to combine amounts (example usage).

Custom Exceptions: InsufficientFunds, AccountNotFound etc.

Decorators: For logging, transactional behavior in services.