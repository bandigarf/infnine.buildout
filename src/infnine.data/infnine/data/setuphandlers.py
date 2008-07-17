from StringIO import StringIO

def importVarious(context):
    """
    Import various settings.

    Provisional handler that does initialization that is not yet taken
    care of by other handlers.
    """
    out = StringIO()
    site = context.getSite()
    
    print >> out, "nothing so far"
    
    logger = context.getLogger("infnine.data")
    logger.info(out.getvalue())
