


SELECT_MULTIPLE = f"""
    SELECT upper(encode("{FIELD_HASH}", 'hex')), "{FIELD_SONG_ID}", "{FIELD_OFFSET}"
    FROM "{FINGERPRINTS_TABLENAME}"
    WHERE "{FIELD_HASH}" IN (%s);
    """
    
IN_MATCH = f"decode(%s, 'hex')"
query = self.SELECT_MULTIPLE % ', '.join([self.IN_MATCH] * len(values[index: index + batch_size]))

cur.execute(query, values[index: index + batch_size])