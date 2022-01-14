class UnknownStatisticsTypeError(Exception):
    """Unknown statistics type.
        
        The specified type does not exist.
        It is likely, that is not implemented or that the data used to build it are corrupted.
        """
    pass
