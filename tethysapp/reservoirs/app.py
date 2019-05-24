from tethys_sdk.base import TethysAppBase, url_map_maker

# todo make the update button not ask for login every time (make it work on the server???)
# todo record demonstration videos

# todo OPTIONAL- improve the written instructions section
# todo OPTIONAL- create a persistent store of old reports and email/download/print option (header button)
# todo OPTIONAL- let the user toggle between elevations and depths on the historical charts
# todo OPTIONAL- add hydrologic factors to analysis like evaporation or infiltration?

class Reservoirs(TethysAppBase):
    """
    Tethys app class for Reservoir Manager Tool.
    """

    name = 'Reservoir Manager Tool'
    index = 'reservoirs:home'
    icon = 'reservoirs/images/reservoir.jpg'
    package = 'reservoirs'
    root_url = 'reservoirs'
    color = '#16a085'
    description = 'Place a brief description of your app here.'
    tags = 'reservoirs, hydrology, streamflow prediction'
    enable_feedback = False
    feedback_emails = []
    currentpage = ''        # a custom attribute added for keeping track of which reservoir is being viewed
    youtubelink = ''        # link to the tutorials

    def url_maps(self):
        UrlMap = url_map_maker(self.root_url)

        url_maps = (

            # OVERVIEW PAGES
            UrlMap(
                name='home',
                url='reservoirs',
                controller='reservoirs.controllers.home'
            ),
            UrlMap(
                name='reportar',
                url='reservoirs/reportar',
                controller='reservoirs.controllers.reportar'
            ),
            UrlMap(
                name='instrucciones',
                url='reservoirs/instrucciones',
                controller='reservoirs.controllers.instructions'
            ),

            # SIMULATIONS PAGES
            UrlMap(
                name='simulations',
                url='reservoirs/simulaciones',
                controller='reservoirs.controllers.simulations'
            ),

            # RESERVOIR SPECIFIC PAGES
            UrlMap(                     # this is the controller for the page that shows reservoir specific stats
                name='template',        # {name} is an argument the controller needs to accept second
                url='reservoirs/{name}',
                controller='reservoirs.controllers.reservoirviewer'
            ),

            # CONTROLLERS FOR AJAX PAGES
            UrlMap(
                name='historicalchart',
                url='reservoirs/ajax/reshistplot',
                controller='reservoirs.ajax.reservoirhistoricalplot'
            ),
            UrlMap(
                name='storageplot',
                url='reservoirs/ajax/resstorageplot',
                controller='reservoirs.ajax.reservoirstorageplot'
            ),
            UrlMap(
                name='overview',
                url='reservoirs/ajax/overviewpage',
                controller='reservoirs.ajax.overviewpage'
            ),
            UrlMap(
                name='simulationtable',
                url='reservoirs/ajax/simulationTable',
                controller='reservoirs.ajax.simulationtable'
            ),
            UrlMap(
                name='getsfptflows',
                url='reservoirs/ajax/getSFPTflows',
                controller='reservoirs.ajax.getsfptflows'
            ),
            UrlMap(
                name='reservoirstatistics',
                url='reservoirs/ajax/reservoirstatistics',
                controller='reservoirs.ajax.reservoirstatistics'
            ),
            UrlMap(
                name='updatesheet',
                url='reservoirs/ajax/updatesheet',
                controller='reservoirs.ajax.updatesheet'
            ),
            UrlMap(
                name='performsimulation',
                url='reservoirs/ajax/performsimulation',
                controller='reservoirs.ajax.performsimulation'
            ),
        )

        return url_maps
