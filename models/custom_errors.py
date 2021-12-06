class UnknownStatisticsTypeError(Exception):
    """Unknown statistics type.
        
        The specified type does not exists.
        It is likely, that is is not implemented or that the data used to build it are corrupted.         
        """
    pass
