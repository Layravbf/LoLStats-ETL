import logging
import boto3
from api import LeagueQueuesApi
import json

# Configuração de Logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Configuração do S3
s3_client = boto3.client('s3')
BUCKET_NAME = 'projeto-layra-how-riot-api'

def save_to_s3(data, filename):
    json_data = '\n'.join(json.dumps(item, ensure_ascii=False) for item in data)
    s3_client.put_object(Body=json_data, Bucket=BUCKET_NAME, Key=filename)

# Função principal
def main():
    ranks_with_divisions = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND"]
    divisions = ["I", "II", "III", "IV"]
    
    ranks_without_divisions = ["MASTER", "GRANDMASTER", "CHALLENGER"]
    
    for rank in ranks_with_divisions:
        for division in divisions:
            for page in range(1, 4):  # Para pegar as 3 primeiras páginas
                data = LeagueQueuesApi(queue="RANKED_SOLO_5x5").get_data(tier=rank, division=division, page=page)
                filename = f"lol_data/{rank}/{division}/data_page_{page}.json"
                save_to_s3(data, filename)
                logger.info(f"Data for {rank} {division} page {page} saved to S3 at {filename}.")
    
    for rank in ranks_without_divisions:
        for page in range(1, 4):  # Para pegar as 3 primeiras páginas
            data = LeagueQueuesApi(queue="RANKED_SOLO_5x5").get_data(tier=rank, division='I', page=page)
            filename = f"lol_data/{rank}/I/data_page_{page}.json"
            save_to_s3(data, filename)
            logger.info(f"Data for {rank} I page {page} saved to S3 at {filename}.")

if __name__ == "__main__":
    main()