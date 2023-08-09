from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.containerregistry.models import Sku

subscription_id = 'b1d7df6c-a5d4-44a8-83c9-07b17ba2b5cb'
resource_group_name = 'yjh'
registry_name = 'yjhmonitoringregistry'
client_id ='871609ca-add3-432f-bca3-e9584d20c6c2'
tenant_id = '20f62116-4d0c-44ac-8a45-390ca2765601'
client_secret = 'zMC8Q~gX_je8PdDwVxj71i9audWuRZllcUbTkbNJ'

credentials = ServicePrincipalCredentials(
    client_id=client_id,
    secret=client_secret,
    tenant=tenant_id
)

client = ContainerRegistryManagementClient(credentials, subscription_id)

registry_sku = Sku(name='Standard')

registry_poller = client.registries.create(
    resource_group_name,
    registry_name,
    {
        "location": "East US",  # Replace with your desired location
        "sku": registry_sku
    }
)

registry=registry_poller.result()

print(f"Container Registry '{registry.name}' created in '{registry.location}'")

